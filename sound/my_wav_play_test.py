try:
    import sounddevice as sd
    import soundfile as sf
    fn = "piano2.wav"
    dev = None
    data, fs = sf.read(fn, dtype='float32')
    sd.play(data, fs, device=dev)
    status = sd.wait()
    if status:
        print('Error during playback: ' + str(status))
except KeyboardInterrupt:
    print('\nInterrupted by user')
except Exception as e:
    print(type(e).__name__ + ': ' + str(e))
