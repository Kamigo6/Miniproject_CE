import numpy as np
import matplotlib.pyplot as plt

# Define the frequency of the two carriers
f1 = 2
f2 = 4

# Define the sample rate
fs = 100

# Define the time axis
t = np.arange(0, 1, 1/fs)

# Generate the two carrier signals
carrier1 = np.sin(2*np.pi*f1*t)
carrier2 = np.sin(2*np.pi*f2*t)

# Plot the two carrier signals
plt.figure()
plt.plot(t, carrier1, label='Carrier 1')
plt.plot(t, carrier2, label='Carrier 2')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()

# Define the number of data bits
N = 5

# Generate a random binary data sequence
data = np.random.randint(0, 2, N)

# Plot the binary data sequence
plt.figure()
plt.stem(data, use_line_collection=True)
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.show()

# Initialize the modulated signal
modulated_signal = np.zeros(int(N*fs))

# Perform the FSK modulation
for i in range(N):
    if data[i] == 0:
        modulated_signal[int(i*fs):int((i+1)*fs)] = carrier1
    else:
        modulated_signal[int(i*fs):int((i+1)*fs)] = carrier2

# Plot the modulated signal
plt.figure()
plt.plot(modulated_signal)
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.show()