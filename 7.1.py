#7.1 Realize the function y=2+5sin(2πft) for f=1KHz, plot it and write it as a .csv file
import numpy as np
from matplotlib import pyplot as plt
t = np.arange(0, 0.002, 0.00002)
f=1000
y = 2+5*np.sin(2*np.pi*f*t)
plt.title("Function",color="r")
plt.plot(t,y,color="purple")
plt.xlabel("time",color="blue")
plt.ylabel("y",color="green")
plt.show()
np.savetxt('waveform.csv', y, delimiter=',')