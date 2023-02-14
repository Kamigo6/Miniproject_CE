import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc #erfc/Q function

# Generate the binary data sequence
# binary_data: The binary data sequence that will be modulated.
binary_data = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0] 

# Constants
A = 1 # The Amplitude of signal
nb = 200 # Number of sampler per bit
N = nb * len(binary_data) # The number of samples in the time domain.
f1 = 40 # The frequency of the first carrier signal. 
f2 = 20 # The frequency of the second carrier signal
t = np.linspace(0, 1, N) # The time vector, generated using the numpy function "linspace" from 0 to 1 with N samples.
N0 = 2 # The power spectral density of the Gaussian noise.

# Generate the carrier signals
# carrier1: The first carrier signal, generated using the numpy cosine function with 2pif1*t as the argument.
carrier1 = A*np.cos(2*np.pi*f1*t) 
# carrier2: The second carrier signal, generated using the numpy cosine function with 2pif2*t as the argument.
carrier2 = A*np.cos(2*np.pi*f2*t) 

def FSKmod(binary_seq):
    mod_signal = []
    Tb = 0
    binary_signal = []

    for i in range(0 ,len(binary_seq)):
        #this loop iterates bitlen times for each bit
        for j in range(Tb, Tb + nb):
            #this loop iterates nb times for each bit (once for each sample)
            if binary_seq[i] == 1:
                #append coswave for bit 1 --- nb samples 
                mod_signal.append(A*np.cos(2*np.pi*f1*t[j]))
            else:
                #append 0 for bit 0 --- nb samples
                mod_signal.append(A*np.cos(2*np.pi*f2*t[j]))
            binary_signal.append(binary_seq[i])
            Tb+=1
    return mod_signal, binary_signal

def ML_criterion(received_signal, carrier, i):
    decision_variable = np.sum(received_signal[i*nb : (i+1)*nb] * carrier[i*nb : (i+1)*nb])
    energy = np.sum(carrier[i*nb : (i+1)*nb]*carrier[i*nb : (i+1)*nb])
    sr = decision_variable - energy/2
    return sr

def FSKdemod(received_signal):
    bitstream =[]
    i = 0
    for i in range(0 ,len(binary_data)):
        if (ML_criterion(received_signal, carrier1, i) > ML_criterion(received_signal, carrier2, i)):
            bitstream.append(1)
        else: 
            bitstream.append(0)
    return bitstream

mod_signal, binary_signal = FSKmod(binary_data)

#Plot
fig = plt.plot(carrier1)
plt.show()

fig = plt.plot(carrier2)
plt.show()

fig = plt.plot(binary_signal)
plt.show()

fig = plt.plot(mod_signal)
plt.show()

binary_len = len(binary_data)
noise = 15*np.sqrt(N0/2)*np.random.randn(len(binary_data) * nb)
sig_noisy= mod_signal + noise
fig = plt.plot(sig_noisy)
plt.show()

r = FSKdemod(mod_signal)
print(*FSKdemod(mod_signal))
print(*binary_data)

error = np.sum(np.abs(np.array(binary_data) - np.array(r))) / len(binary_data) 
print("%5.2f%%" % (error*100))

#BER

Pe_bpsk = 0.5*erfc(np.sqrt(10**(EbN0dBs/10)))
Pe_bfsk = 0.5*erfc(np.sqrt(10**(EbN0dBs/10)/2))
Pe_bask = 0.5*erfc(np.sqrt(10**(EbN0dBs/10)/4))


fig, ax = plt.subplots(nrows=1,ncols = 1)
ax.semilogy(EbN0dBs,Pe_bpsk,marker='',linestyle='-',label='BPSK Theory')
ax.semilogy(EbN0dBs,Pe_bfsk,marker='',linestyle='-',label='BFSK Theory')
ax.semilogy(EbN0dBs,Pe_bask,marker='',linestyle='-',label='BASK Theory')

ax.set_xlabel('$E_b/N_0(dB)$');ax.set_ylabel('BER ($P_b$)')
ax.set_title('Probability of Bit Error for BPSK, BFSK, BASK over AWGN channel')
ax.set_xlim(-5,13);ax.grid(True);
ax.legend();
plt.savefig('./ber.jpg')

plt.show()