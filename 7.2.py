#7.2 Read the given .csv file as an array and plot it. Compute the mean and standard deviation of the
#signal. Plot its histogram with an appropriate bin size.
import numpy as np
from matplotlib import pyplot as plt
y=np.genfromtxt('waveform.csv',delimiter=',')
#Mean and Standard deviation
m=np.mean(y)
print(m)
sd=np.std(y)
print(sd)
fig,a = plt.subplots(2,1)
a[0].plot(y,color="maroon")
a[0].set_title('Waveform',color="r")
a[1].hist(y, bins = [-5,-4, -3, -2, -1, 0, 1, 2, 3, 4, 5,6,7,8,9],color="purple")
a[1].set_title('Histogram',color="blue")
plt.show() 