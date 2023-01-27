import numpy as np
import matplotlib.pyplot as plt

# Generate a random binary sequence of 16 bits
binary_seq = np.random.randint(0, 2, 16)

# Define the frequency for binary 0 and binary 1
f0 = 5
f1 = 10

# Generate the time vector
t = np.linspace(0, len(binary_seq), len(binary_seq))

# Generate the FSK signal by multiplying the binary sequence with the appropriate frequency
fsk_signal = np.zeros(len(binary_seq))
fsk_signal[binary_seq == 0] = np.sin(2*np.pi*f0*t)
fsk_signal[binary_seq == 1] = np.sin(2*np.pi*f1*t)

# Generate the carrier signal
carrier_signal = np.sin(2*np.pi*f0*t)

# Plot the binary data sequence, carrier signal and FSK modulate signal
fig, axs = plt.subplots(3, 1, sharex=True, sharey=True)
axs[0].stem(t, binary_seq, '-o', linefmt='C0')
axs[0].set_title('Binary data sequence')
axs[1].plot(t, carrier_signal)
axs[1].set_title('Carrier signal')
axs[2].plot(t, fsk_signal)
axs[2].set_title('FSK modulated signal')

plt.xlabel('Time (s)')
plt.show()

#save the figure as an image
plt.savefig("fsk_modulation.png")