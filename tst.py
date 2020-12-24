import numpy as np
import matplotlib.pyplot as plt
from numpy import random
M=15
x = np.arange(0, M, 1)
y=random.randint(11, size=(M))
fi,a= plt.subplots(3,1)
a[0].plot(x,y)
a[0].plt.boxplot(y)
a[0].plt.title('BOX PLOT')
a[0].plt.legend(['XY Box Plot'])
plt.show()