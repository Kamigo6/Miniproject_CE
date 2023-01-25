import matplotlib.pyplot as plt
import numpy as np


fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(15, 8))
fig.subplots_adjust(hspace=0.5)

t = np.arange(0,2,0.001)
symbols = np.array([1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0])

train = np.repeat(symbols, 100)
ax1.plot(t,train)
ax1.set_title("Binary Data Sequence")
ax1.set_ylabel("Amplitude")
ax1.set_ylim(bottom=0, top=2.5)
ax1.set_xlim(left=0, right=2)
for i, symbol in enumerate(symbols):
    ax1.text(i/10+0.035, 1.5, str(symbol), fontsize=14, color='red')

f = 25
x = np.cos(2*np.pi*f*t)*np.ones(2000)
ax2.plot(t,x)
ax2.set_title("Carrier Signal")
ax2.set_xlabel("Time")
ax2.set_ylabel("Amplitude")
ax2.set_xlim(left=0, right=2)

y = np.cos(2*np.pi*f*t)*train
ax3.plot(t, y)
ax3.set_title("ASK Modulated Signal")
ax3.set_xlabel("Time")
ax3.set_ylabel("Amplitude")
ax3.set_xlim(left=0, right=2)

plt.show()

fig.savefig('D:\TestProjectCe\\textbook-master\mywork\img\Ask.png', bbox_inches='tight')
