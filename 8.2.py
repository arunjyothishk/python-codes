import numpy as np
import matplotlib.pyplot as plt
import math
T=20
t = np.arange(0, 40, 0.01) # arguments: start, stop, step
N=[3,5,10,20]
fig,a = plt.subplots(4,1)
i=0
for value in N:
    sum=1
    for n in range(1, value):
        term = ((-1)**n)*1/(2*n+1)*np.cos(2*math.pi*(2*n+1)*t/T)
        sum=sum+term
    y =(4/math.pi)*(1+sum)
    a[i].plot(t,y)
    a[i].set_title('y')
    i+=1
plt.show()