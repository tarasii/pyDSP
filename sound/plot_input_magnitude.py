#!/usr/bin/env python3
"""Plot the live microphone signal(s) with matplotlib.

Matplotlib and NumPy have to be installed.

"""
import argparse
import queue
import sys


def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    '-l', '--list-devices', action='store_true',
    help='show list of audio devices and exit')
parser.add_argument(
    '-d', '--device', type=int_or_str,
    help='input device (numeric ID or substring)')
parser.add_argument(
    '-w', '--window', type=float, default=200, metavar='DURATION',
    help='visible time slot (default: %(default)s ms)')
parser.add_argument(
    '-i', '--interval', type=float, default=30,
    help='minimum time between plot updates (default: %(default)s ms)')
parser.add_argument(
    '-b', '--blocksize', type=int, help='block size (in samples)')
parser.add_argument(
    '-r', '--samplerate', type=float, help='sampling rate of audio device')
parser.add_argument(
    '-n', '--downsample', type=int, default=10, metavar='N',
    help='display every Nth sample (default: %(default)s)')
parser.add_argument(
    'channels', type=int, default=[1], nargs='*', metavar='CHANNEL',
    help='input channels to plot (default: the first)')
args = parser.parse_args()
if any(c < 1 for c in args.channels):
    parser.error('argument CHANNEL: must be >= 1')
mapping = [c - 1 for c in args.channels]  # Channel numbers start with 1
q = queue.Queue()


def audio_callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    # Fancy indexing with mapping creates a (necessary!) copy:
    q.put(indata[::args.downsample, mapping])


def update_plot(frame):
    """This is called by matplotlib for each plot update.

    Typically, audio callbacks happen more frequently than plot updates,
    therefore the queue tends to contain multiple blocks of audio data.

    """
    global plotdata
    global magnitude
    while True:
        try:
            data = q.get_nowait()
        except queue.Empty:
            break
        shift = len(data)
        plotdata = np.roll(plotdata, -shift, axis=0)
        plotdata[-shift:, :] = data

    for column, line in enumerate(lines[0]):
        line.set_ydata(plotdata[:, column])
    for column, line in enumerate(lines[1]):
        magnitude = 20 * np.log10(2 * np.abs(np.fft.fft(plotdata[:, column])[:len(plotdata)//2]))
        line.set_ydata(magnitude)

    return lines


try:
    from matplotlib.animation import FuncAnimation
    import matplotlib.pyplot as plt
    import numpy as np
    import sounddevice as sd

    if args.list_devices:
        print(sd.query_devices())
        parser.exit(0)
    if args.samplerate is None:
        device_info = sd.query_devices(args.device, 'input')
        args.samplerate = device_info['default_samplerate']

    length = int(args.window * args.samplerate / (1000 * args.downsample))
    plotdata = np.zeros((length, len(args.channels)))
    magnitude = np.zeros((length//2, len(args.channels)))
    print(length)

    k = np.arange(length)
    T = length/args.samplerate*args.downsample
    freq = k/T # two sides frequency range
    freq = freq[:length//2]

    fig, ax = plt.subplots(2,1)
    lines = [ax[0].plot(plotdata,'g'), ax[1].plot(freq, magnitude)]

    if len(args.channels) > 1:
        ax.legend(['channel {}'.format(c) for c in args.channels],
                  loc='lower left', ncol=len(args.channels))
    ax[0].axis((0, len(plotdata), -1, 1))
    ax[0].set_yticks([0])
    ax[0].yaxis.grid(True)
    ax[0].tick_params(bottom='off', top='off', labelbottom='off',
                   right='off', left='off', labelleft='off')

    ax[1].axis((0, freq[-1], -40, 60))
    ax[1].tick_params(bottom='off', top='off', labelbottom='off',
                   right='off', left='off', labelleft='off')

    fig.tight_layout(pad=0)
    print(args.window)
    print(args.downsample)
    print(args.device)
    print(args.channels)
    print(args.samplerate)
    print(args.interval)
    stream = sd.InputStream(
        device=args.device, channels=max(args.channels),
        samplerate=args.samplerate, callback=audio_callback)
    ani = FuncAnimation(fig, update_plot, interval=args.interval, blit=False)

    with stream:
        plt.show()

except Exception as e:
    parser.exit(type(e).__name__ + ': ' + str(e))
