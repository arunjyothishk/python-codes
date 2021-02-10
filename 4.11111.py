import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,2*np.pi,180)
y=np.sin(x)
a=np.cos(x)
b=np.sinh(x)
d=np.cosh(x)
e=np.tan(x)
# b=np.sinht(x)

def der(y):

    c=2*np.pi/180
    frst_der= np.gradient(y,c)
    secnd_der=np.gradient(frst_der,c)

    plt.plot(x,y,'g',label='Og fn')
    plt.plot(x,frst_der,'r',label='First Derivative')
    plt.plot(x,secnd_der,label='Second Derivative')
    plt.legend(loc='upper left')
    plt.show()

# der(y)
der(a)
# der(b)
# der(d)
# der(e)
