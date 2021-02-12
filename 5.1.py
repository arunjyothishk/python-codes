#differential equation dx/dt+2x = 0

import numpy as np
from scipy.integrate import odeint #
import matplotlib.pyplot as plt


# function that returns dx/dt
def diff_equation(x,t):
 dxdt = -2 * x
 return dxdt


# initial condition
x0 = 1
# time points
t = np.linspace(0,10)
# solve ODE
y = odeint(diff_equation,x0,t)
# plot results
plt.plot(t,y)
plt.xlabel('time')
plt.ylabel('x(t)')
plt.title('solution for first order ode')
plt.show()