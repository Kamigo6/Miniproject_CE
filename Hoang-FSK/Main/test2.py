import numpy as np
import matplotlib.pyplot as plt

# FSK parameters
fs = 1000 # sample rate
f1 = 2 # frequency for binary 0
f2 = 4 # frequency for binary 1
T = 1 # duration of one bit
N = int(fs*T) # number of samples

# Generating the Carrier Signals
t = np.linspace(0, T, N, endpoint=False)
carrier1 = np.sin(2*np.pi*f1*t)
carrier2 = np.sin(2*np.pi*f2*t)

# Generating the Binary Data Sequence
data = np.random.randint(0, 2, N)

# FSK Modulation
modulated = np.zeros(N)
for i in range(N):
    if data[i] == 0:
        modulated[i] = carrier1[i]
    else:
        modulated[i] = carrier2[i]

# Adding Gaussian Noise
noise = np.random.normal(0, 0.1, N)
modulated_noise = modulated + noise

# Plotting the Results
plt.figure()
plt.subplot(4, 1, 1)
plt.plot(t, carrier1, 'r')
plt.title('Carrier Signal 1 (f1 = 200Hz)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.subplot(4, 1, 2)
plt.plot(t, carrier2, 'g')
plt.title('Carrier Signal 2 (f2 = 300Hz)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.subplot(4, 1, 3)
plt.plot(t, modulated, 'b')
plt.title('FSK Modulated Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.subplot(4, 1, 4)
plt.plot(t, modulated_noise, 'k')
plt.title('FSK Modulated Signal with Gaussian Noise')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()