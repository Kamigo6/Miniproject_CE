import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Generate binary data sequence
data = np.random.randint(0, 2, size=1000)

# Define carrier frequencies
f1 = 5
f2 = 10

# Generate carrier signals
fs = 1000 # sample rate
t = np.arange(0, len(data) / fs, 1/fs)
carrier1 = np.sin(2 * np.pi * f1 * t)
carrier2 = np.sin(2 * np.pi * f2 * t)

# Perform FSK modulation
modulated_sig = np.zeros(len(t))
modulated_sig[data == 0] = carrier1[data == 0]
modulated_sig[data == 1] = carrier2[data == 1]

# Add Gaussian noise to the modulated signal
noise = np.random.normal(0, np.sqrt(10), size=len(modulated_sig))
noisy_sig = modulated_sig + noise

# Perform FSK demodulation
decision_variables = signal.correlate(noisy_sig, carrier1, mode='same')
demodulated_data = np.zeros(len(data))
demodulated_data[decision_variables >= 0] = 0
demodulated_data[decision_variables < 0] = 1

# Plot the results
plt.figure()
plt.plot(data, 'b-', label='Original Data')
plt.plot(demodulated_data, 'r-', label='Demodulated Data')
plt.xlabel('Sample index')
plt.ylabel('Data value')
plt.legend()
plt.show()