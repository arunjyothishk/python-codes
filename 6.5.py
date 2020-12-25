# import numpy as np
# import matplotlib.pyplot as plt
# #array-generating functions
# t = np.arange(-10, 10, 0.01) 
# # arguments: start, stop, 
# stepy1 = np.cos(t)
# y2 = 
# fig,a=  plt.subplots(2,1)
# a[0].plot(t,y1)
# a[0].set_title('Cost')
# plt.show() 

import numpy as np
import matplotlib.pyplot as plot
t = np.arange(-10,10,0.01)
y1 = np.cos(t)
y2 = np.cos(t)*np.cos(5*t)+np.cos(5*t)
fig,a=plot.subplots(2,1)
a[0].plot(t,y1)
a[0].set_title('cos(t)')
a[1].plot(t,y2)
a[1].set_title('costcos5t+cos5t')
plot.show()

