import time
from numpy import *
a = arange(0,1000)
print(a)
b = arange(1000,2000)

def call():
    
    outer_product = zeros((1000, 1000))
    for i in range(len(a)):
        for j in range(len(b)):
            outer_product[i][j]= a[i]*b[j]
    return outer_product
# classic implementation
tic = time.process_time()
outer_product=call()
toc = time.process_time()
print("outer_product classic = "+ str(outer_product));
print("Computation time = "+str(1000*(toc - tic ))+"ms")
print("///////")
#vectorized computing
n_tic = time.process_time()
outer_product = outer(a, b)
n_toc = time.process_time()
print("outer_product   vector = "+str(outer_product));
print("\nComputation time = "+str(1000*(n_toc - n_tic ))+"ms")

