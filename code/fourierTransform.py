import numpy as np #importing a library
import matplotlib.pyplot as plt #importing a library
pi = np.pi #get pi
e = np.exp #get e^ function
sr = 44100. #sample rate
N = 1024 #length in smaples
lenSec = N/sr #length in seconds

f = 1000 #frequency of sine wave to generate
t = np.linspace(0,lenSec, N) # time array
x = np.sin(t*2*pi*f) #making a sine wave as input signal

xf = np.zeros_like(x,dtype=np.complex_) #initializing complex output array of zeros

# Actual Discrete Fourier Transform
for m in range(N): #looping over all frequencies
    for n in range(N): #looping over the whole input signal
        xf[m] = xf[m]+x[n]*e(-1j*2*pi*n*m/N)

#======plotting===================
plt.subplot(211)
plt.plot(x) #plotting the input
plt.xlabel('time [samples]')
plt.title('input, time domain')
plt.subplot(212)
plt.plot(abs(xf)) #plotting the magnitude spectrum (two-sided)
plt.xlabel('frequency [bins/samples]')
plt.title('output, frequency domain')
plt.show() #displaying the output plot
