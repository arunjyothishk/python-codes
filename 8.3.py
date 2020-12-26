import numpy as np
import matplotlib.pyplot as plt
import math
T=20
N=[5,10,100,1000]
i=0
for value in N:
    sum=1
    for n in range(1, value):
        term = ((-1)**n)*1/(2*n+1)
        sum=sum+term
    pi_value =4*sum
    print(pi_value)
    i+=1