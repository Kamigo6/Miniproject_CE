#BER
import numpy as np #for numerical computing
import matplotlib.pyplot as plt #for plotting functions
from scipy.special import erfc #erfc/Q function

#---------Input Fields------------------------
EbN0dBs = np.arange(start=-10,stop = 13, step = 1) # Eb/N0 range in dB for simulation

Pe_bpsk = 0.5*erfc(np.sqrt(10**(EbN0dBs/10)))
Pe_bfsk_bask = 0.5*erfc(np.sqrt(10**(EbN0dBs/10)/2))

fig, ax = plt.subplots(nrows=1,ncols = 1)
ax.semilogy(EbN0dBs,Pe_bpsk,marker='',linestyle='-',label='BPSK Theory')
ax.semilogy(EbN0dBs,Pe_bfsk_bask,marker='',linestyle='-',label='BFSK/BASK Theory')
# ax.semilogy(EbN0dBs,Pe_bask,marker='',linestyle='-',label='BASK Theory')

ax.set_xlabel('$E_b/N_0(dB)$');ax.set_ylabel('BER ($P_b$)')
ax.set_title('Probability of Bit Error for BPSK, BFSK, BASK over AWGN channel')
ax.set_xlim(-11,13);ax.grid(True);
ax.legend();
plt.savefig('D:\Miniproject_Ce\Dat_PSK\pic\ls_ber.jpg')

plt.show()