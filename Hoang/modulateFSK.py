import numpy as np
import matplotlib.pyplot as plt

# Generate a random binary sequence with length 10
binary_seq = np.random.randint(0, 2, 10)

# Define the carrier frequency for the 0s and 1s in the sequence
f0 = 1000
f1 = 2000

# Define the bit rate
bit_rate = 10000

# Generate the time vector for the signal
t = np.linspace(0, len(binary_seq)/bit_rate, len(binary_seq)*bit_rate)

# Initialize an empty signal array
signal = np.zeros(len(binary_seq)*bit_rate)

# Define the carrier signal
carrier_signal = np.sin(2*np.pi*f0*t)

# Modulate the binary sequence onto the carrier signal
for i, bit in enumerate(binary_seq):
    if bit == 1:
        carrier_signal[i*bit_rate:(i+1)*bit_rate] = np.sin(2*np.pi*f1*t[i*bit_rate:(i+1)*bit_rate])

# Create a figure with 3 subplots
fig, (ax1, ax2, ax3) = plt.subplots(3,1, figsize=(8,8))

# Plot the FSK signal
ax1.plot(t, carrier_signal)
ax1.set_title('FSK Signal')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Amplitude')

# Plot the binary data sequence
ax2.stem(np.arange(10), binary_seq)
ax2.set_title('Binary Data Sequence')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Amplitude')

# Plot the carrier signal for 0s
ax3.plot(t, np.sin(2*np.pi*f0*t))
ax3.set_title('Carrier Signal for 0s')
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Amplitude')

# Save the plot as an image
plt.savefig('FSK_signal_with_data_sequence_carrier_3subplots.png')