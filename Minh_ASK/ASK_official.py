import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('ggplot')

def ASKmod(binary_seq):
    mod_signal = []
    Tb = 0
    binary_signal = []

    for i in range(0 ,len(binary_seq)):
        #this loop iterates bitlen times for each bit
        for j in range(Tb, Tb + nb):
            #this loop iterates nb times for each bit (once for each sample)
            if binary_seq[i] == 1:
                #append coswave for bit 1 --- nb samples 
                mod_signal.append(A1*np.cos(2*np.pi*f*timeline[j]))
            else:
                #append 0 for bit 0 --- nb samples
                mod_signal.append(A2*np.cos(2*np.pi*f*timeline[j]))
            binary_signal.append(binary_seq[i])
            Tb+=1
    return mod_signal, binary_signal

def ML_criterion(received_signal, carrier, i):
    decision_variable = np.sum(received_signal[i*nb : (i+1)*nb] * carrier[i*nb : (i+1)*nb])
    energy = np.sum(carrier[i*nb : (i+1)*nb]*carrier[i*nb : (i+1)*nb])
    sr = decision_variable - energy/2
    return sr

def ASKdemod(received_signal):
    bitstream =[]
    i = 0
    for i in range(0 ,len(binary_seq)):
        if (ML_criterion(received_signal, carrier1, i) > ML_criterion(received_signal, carrier2, i)):
            bitstream.append(1)
        else: 
            bitstream.append(0)
    return bitstream
def disp():
    #Plotting the signals
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 5))
    fig.subplots_adjust( hspace = 0.5)

    #Plot binary sequence
    ax1.plot(timeline, binary_signal)
    ax1.set_title("Binary Data Sequence")
    ax1.set_ylim(bottom=-0.5, top=1.5)
    ax1.set_ylabel("Amplitude")

    #Plot modulated signal
    ax2.plot(timeline, mod_signal)
    ax2.set_title("ASK Modulated Signal")
    ax2.set_xlabel("Time period")
    ax2.set_ylabel("Amplitude")

    # plt.show()
    fig.savefig('D:\Miniproject_Ce\Minh_ASK\pic\Modulate_ask.png', bbox_inches='tight')

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 5))
    fig.subplots_adjust( hspace = 0.5)
    
    #Plot carrier signal
    ax1.plot(timeline, carrier1)
    ax1.set_title("Carrier Signal 1")
    ax1.set_xlabel("Time period")
    ax1.set_ylabel("Amplitude")

    ax2.plot(timeline, carrier2)
    ax2.set_title("Carrier Signal 2")
    ax2.set_xlabel("Time period")
    ax2.set_ylabel("Amplitude")
    ax2.set_ylim(bottom=-10, top=10)

    # plt.show()
    fig.savefig('D:\Miniproject_Ce\Minh_ASK\pic\Carriers_ask.png', bbox_inches='tight')

    fig, (ax1) = plt.subplots(1, 1, figsize=(10, 4))
    fig.subplots_adjust( hspace = 0.5)
    #Plot noisy signal
    ax1.plot(timeline, noisy_signal)
    ax1.set_title("Noisy Received Signal")
    ax1.set_xlabel("Time period")
    ax1.set_ylabel("Amplitude")
    # plt.show()
    fig.savefig('D:\Miniproject_Ce\Minh_ASK\pic\Demodulate_AWGN_ask.png', bbox_inches='tight')
   

# bitlen = 200
nb = 100  # number of samples per bit
A1 = 20 # Carrier1 signal amplitude 
A2 = 0  # Carrier2 signal amplitude  
f = 5  # Carrier signal frequency
N0 = 1000 # The power spectral density of the Gaussian noise
# binary_seq = [random.randint(0,1) for x in range(0,bitlen)]
# the binary sequence
binary_seq = np.array([1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0]) 
bitlen = len(binary_seq) # the length of binary sequence
print('The input binary sequence is : {}\n'.format(binary_seq))

timeline = np.arange(0 , bitlen, 0.01)
carrier1 = A1*np.cos(2*np.pi*f*timeline)
carrier2 = A2*np.cos(2*np.pi*f*timeline)

mod_signal, binary_signal = ASKmod(binary_seq)

noise = 10*np.sqrt(N0/2)*np.random.randn(bitlen * nb)
noisy_signal= mod_signal + noise

binary_demod_noisy = ASKdemod(noisy_signal)
binary_demod = ASKdemod(mod_signal)

disp()

error = np.sum(np.abs(binary_seq - binary_demod_noisy)) / bitlen
print("%5.2f%%" % (error*100))
