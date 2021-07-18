import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt


import soundfile as sf
data, fs = sf.read("piano2.wav", dtype='float32')
#sd.play(data, fs)
#status = sd.wait()
#if status:
#    parser.exit('Error during playback: ' + str(status))

#f = 100
#q = 44100
#t = 2
#myarray = [2*np.pi*x*f/q for x in range(0, t*q)]
#myarray = np.sin(myarray)

f1 = 1000
f2 = 700
q = 44100
t = 5
phi1 = [2*np.pi*x*f1/q for x in range(0, t*q)]
phi2 = [2*np.pi*x*f2/q for x in range(0, t*q)]
myarray = np.sin(phi1)+np.sin(phi2)


#print(myarray)

plt.plot(myarray[:1000])
#plt.plot(data)
#plt.show()

sd.play(myarray, q)
status = sd.wait()
if status:
    parser.exit('Error during playback: ' + str(status))

