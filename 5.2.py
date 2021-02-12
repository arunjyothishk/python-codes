#5.2 Solve for the current transient through an RC network (with RC = 3) that is driven by
#(a) 5 V DC (b) the signal 5e–t U(t) and plot the solutions. 


#(A) 5 V DC
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
# function that returns dy/dt
def model(i,t):
 didt = -(i/rc)
 return didt
# time
t=np.linspace(0,20)
# initial conditions given
V=5
rc=3
r=3
i0=V/r
# solve ode
OI= odeint(model,i0,t)
#plot results
plt.plot(t,OI)
plt.xlabel('time')
plt.ylabel('current ')
plt.title('current transient response of RC circuit for 5V dc')
plt.show()


#(B)the signal 5e–t U(t)
# function that returns dy/dt
def model1(i,t):
 didt = -((5*math.exp(-t))/r+(i/rc))
 return didt
# time
t=np.linspace(0,20)
# conditions given
rc=3
r=3
V=5
i0=V/r
# solve ode
OI= odeint(model1,i0,t)
#plot results
plt.plot(t,OI)
plt.xlabel('time')
plt.ylabel('current ')
plt.title('current transient response of RC circuit for 5e(-t)u(t)')
plt.show()