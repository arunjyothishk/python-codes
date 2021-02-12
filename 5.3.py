#5.3 Solve the second order differential equation dx^2/dt^2+ 2dx/dt + 2x = e^−t
 
import numpy as np
import math
from scipy.integrate import odeint
import matplotlib.pyplot as plt
def dx_dt(U, t):
 # Here are the eqns
 return [U[1], -2*U[1] - 2*U[0] + math.exp(-t)]
x0 = [0, 0] #inital conditions x[0] & x'[0]
ts = np.linspace(0, 10, 100) #time points from 0 to 10
# solving equations using ode
Us = odeint(dx_dt, x0, ts)
xs = Us[:,0]
# plotting result
plt.xlabel("t")
plt.ylabel("x")
plt.title("solution for second order ode")
plt.plot(ts,xs)
plt.show()