import numpy as np #for numerical computing
import matplotlib.pyplot as plt #for plotting functions
from scipy.special import erfc #erfc/Q function

#---------Input Fields------------------------
nSym = 10**5 # Number of symbols to transmit
EbN0dBs = np.arange(start=-4,stop = 13, step = 1) # Eb/N0 range in dB for simulation
BER_sim = np.zeros(len(EbN0dBs)) # simulated Bit error rates

M=2 #Number of points in BPSK constellation
m = np.arange(0,M) #all possible input symbols
A = 1; #amplitude
#------------ Transmitter---------------
Pe_bpsk = 0.5*erfc(np.sqrt(10**(EbN0dBs/10)))
Pe_bfsk = 0.5*erfc(np.sqrt(10**(EbN0dBs/10)/2))
Pe_bask = 0.5*erfc(np.sqrt(10**(EbN0dBs/10)/4))


fig, ax = plt.subplots(nrows=1,ncols = 1)
ax.semilogy(EbN0dBs,Pe_bpsk,marker='',linestyle='-',label='BPSK Theory')
ax.semilogy(EbN0dBs,Pe_bfsk,marker='',linestyle='-',label='BPSK Theory')
ax.semilogy(EbN0dBs,Pe_bask,marker='',linestyle='-',label='BPSK Theory')

ax.set_xlabel('$E_b/N_0(dB)$');ax.set_ylabel('BER ($P_b$)')
ax.set_title('Probability of Bit Error for BPSK, BFSK< BASK over AWGN channel')
ax.set_xlim(-5,13);ax.grid(True);
ax.legend();
plt.show()