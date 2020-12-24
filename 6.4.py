import numpy as np
import matplotlib.pyplot as plt
#array-generating functions
a=np.array([22,55,43,76,25,27,17,56,71,31,34,56])
plt.hist(a,bins=[0,25,50,75,100])
plt.show()