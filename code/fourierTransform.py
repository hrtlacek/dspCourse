import numpy as np
import matplotlib.pyplot as plt

sr = 44100.
N = 1024 #length in smaples
lenSec = N/sr #length in seconds

f = 1000 #frequency of sine wave to generate
t = np.linspace(0,lenSec, N)
x = np.sin(t*2*np.pi*f) #making a sine wave as input signal

xf = np.zeros_like(x,dtype=np.complex_) #initializing complex array of zeros

# Actual Discrete Fourier Transform
for m in range(N):
    for n in range(N):
        xf[m] = xf[m]+x[n]*np.exp(-1j*2*np.pi*n*m/N)

plt.plot(abs(xf)) #plotting the spectrum (two-sided)
plt.show()
