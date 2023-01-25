import matplotlib.pyplot as plt
import numpy as np
import random
import math
from matplotlib import style
style.use('ggplot')



def FSkgen(inpSig, fskFreq1, fskFreq2):
    #create a time domain from 0 to length of input(bit length) in intervals of 0.01....thus total of 100 samples per bit...hence 1600 samples for 16 bit data.
    timepd = np.arange(0 ,len(inpSig) ,0.01)

    #init arrays mainsig to store output FSK and adjsig array which stores same data as input signal but sampled at 100 samples/bit to plot with timepd
    #lval is just a constant used to iteratively jump 100 samples to next bit at every next iteration, thus looping 16 times for 16 bits.
    mainsig = []
    lval = 0
    adjsig = []


    for i in range(0 ,len(inpSig)):
        #this loop iterates 16 times for each bit
        for j in range(lval,lval+100):
            #this loop iterates 100 times for each bit (once for each sample)
            if inpSig[i]==1:
                #append sinewave with frequency fskFreq1 for bit 1 --- 100 samples 
                mainsig.append( np.sin(2*np.pi*fskFreq1*timepd[j]) )
            else:
                #append sinewave with frequence fskFreq2 for bit 0 --- 100 samples
                mainsig.append( np.sin(2*np.pi*fskFreq2*timepd[j]) )
            adjsig.append(inpSig[i])
            lval+=1
    return timepd, mainsig, adjsig

def FSKdemod(FSKsig):
    sample_duration = len(FSKsig)/16
    i = 0
    #initializing crosscount array to count the number of zero crossings per bit duration(100 samples) and bitstream array to store output demodulated 16 bits
    cross_count = []
    bitstream =[]

    while i<len(FSKsig):
        zero_cross = []

        #reference frame is a frame of continous sampled FSK data representing one bit of 16 bit representation---frames of 100 samples each 
        ref_frame = FSKsig[int(i):int(i+sample_duration)]

        #iterating through the frame , note that we exclude last and first indices...i'll get back to that
        for x in range(1, len(ref_frame)-1 ):
            
            #checking prev and next element to detect zero crossing... this is where the excluded last and first indices are taken in, iteratively going thru [i-1] & [i+1] each step
            if np.logical_and(ref_frame[x-1]<0 , ref_frame[x+1]>0) or np.logical_and(ref_frame[x-1]>0, ref_frame[x+1]<0):
                zero_cross.append(round(ref_frame[x],2))
            else:
                pass
        cross_count.append(len(zero_cross))
        i+=sample_duration
    
    #through trial and error its estimated that there will be more than 5 zero crossings for bit 1, Thersholding crosscount and setting bit values of bitstream accordingly
    #The threshold can be determined more accurately using statistical methods but i decided to omit this step and hardcode instead
    for k in range(0, len(cross_count)):
        if cross_count[k]<5:
            bitstream.append(1)
        else:
            bitstream.append(0)
    
    return bitstream

def awgn(signal):
    regsnr=54
    sigpower=sum([math.pow(abs(signal[i]),2) for i in range(len(signal))])
    sigpower=sigpower/len(signal)
    noisepower=sigpower/(math.pow(10,regsnr/10))
    noise=math.sqrt(noisepower)*(np.random.uniform(-1,1,size=len(signal)))
    return noise

def main():    

    #generating random 16 bit input
    bitlen = 16
    # inpSig = [random.randint(0,1) for x in range(0,bitlen)]
    inpSig = np.array([1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0])
    print('\nthe input binary sequence is : {}\n'.format(inpSig))

    f1 = 1
    f2 = 3
 
    
    #compute FSK of input signal with fskFreq1 for bit1 as 2Hz, fskFreq2 for  bit2 as 0.9Hz...frequencies chosen for better visibility in plots
    timepd, mainsig, adjsig = FSkgen(inpSig,f1,f2)

    time = np.linspace(0, 16, 1600, endpoint=True)

    #Demodulate the FSK signal
    det_Bits = FSKdemod(mainsig)
    bitPlot = []

    #scale detected bits to the same length as timepd...100 samples/bit...1600 samples
    for bit in det_Bits:
        for x in range(0,100):
            bitPlot.append(bit)


    #Plotting the signals
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(15, 8))
    fig.subplots_adjust(hspace=0.5)

    #Plot binary sequence
    ax1.plot(time, adjsig)
    ax1.set_title("Binary Data Sequence")
    ax1.set_ylim(bottom=-0.5, top=1.5)


    #Plot carrier signal
    carrier = np.sin(2*np.pi*(f2+f1)/2*time)
    ax2.plot(time, carrier)
    ax2.set_title("Carrier Signal")
    ax2.set_xlabel("Time")
    ax2.set_ylabel("Amplitude")


    #Plot modulated signal
    ax3.plot(time, mainsig)
    ax3.set_title("FSK Modulated Signal")
    ax3.set_xlabel("Time")
    ax3.set_ylabel("Amplitude")

    plt.show()
    fig.savefig('D:\Miniproject_Ce\mywork\img\Modulate_fsk.png', bbox_inches='tight')

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 8))
    fig.subplots_adjust(hspace=0.5)

    #Plot modulated signal
    ax1.plot(time, mainsig)
    ax1.set_title("FSK Modulated Signal")
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Amplitude")


    #Plot demodulated signal
    ax2.plot(time, bitPlot)
    ax2.set_title("FSK demodulated Signal")
    ax2.set_xlabel("Time")
    ax2.set_ylabel("Amplitude")

    plt.show()
    fig.savefig('D:\Miniproject_Ce\mywork\img\Demodulate_fsk.png', bbox_inches='tight')
if __name__ == "__main__":
    main()

