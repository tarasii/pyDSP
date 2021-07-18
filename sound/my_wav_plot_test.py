import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import soundfile as sf


fn = "piano2.wav"
data, fs = sf.read(fn, dtype='float32')

print (np.shape(data))

plotdata = data[:,0] #take 1 chanell

magnitude = np.abs(np.fft.rfft(plotdata))
#magnitude = np.fft.fft(plotdata[:1024])

fig, (ax, ak, az) = plt.subplots(3,1)

lines = ax.plot(plotdata)
lines1 = ak.plot(magnitude)


#ax.axis((0, len(plotdata), -1, 1))
#ax.set_yticks([0])
#ax.yaxis.grid(True)
#ax.tick_params(bottom='off', top='off', labelbottom='off',
#               right='off', left='off', labelleft='off')

fig.tight_layout(pad=0)
#plt.show()

arr = az.magnitude_spectrum(plotdata)
plt.show()
