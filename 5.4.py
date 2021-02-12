#5.4 Solve the current transient through a series RLC circuit with R = 1Ω, L = 1 mH and C = 1 µF that is
#driven by (a) 5 V DC (b) the signal 5e–tU(t)

#(A)5 V DC
import numpy as np
import math
from scipy.integrate import odeint
import matplotlib.pyplot as plt
V = 5.0 #voltageSource
R = 1.0
L=1.0e-3 #1mH
C = 1.0e-6 #1microF
I=V/R # inital current
def model(i,t):
 return[L*i[1], -R*i[1] - (1/C)*i[0]]
x0 = [I, 0] #inital conditions x[0] & x'[0]
ts = np.linspace(0, 15, 100) #time points from 0 to 10
Us = odeint(model, x0, ts)
xs = Us[:,0]
plt.xlabel("t")
plt.ylabel("i")
plt.title("solution for current in RLC series circuit for dc")
plt.plot(ts,xs)
plt.show()
#(B)the signal 5e–tU(t)
V = 5.0 #voltageSource
R = 1.0
L=1.0e-3 #1mH
C = 1.0e-6 #1microF
I=V/R
def model(i,t):
 return[L*i[1], -R*i[1] - (1/C)*i[0] -5*math.exp(-t)]
x0 = [I, 0] #inital conditions x[0] & x'[0]
ts = np.linspace(0, 5, 100) #time points from 0 to 10
Us = odeint(model, x0, ts)
xs = Us[:,0]
plt.xlabel("t")
plt.ylabel("i")
plt.title("solution for transient current at 5exp(-t) u(t)")
plt.plot(ts,xs)
plt.show()