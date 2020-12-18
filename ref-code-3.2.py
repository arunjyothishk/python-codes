import numpy as np

# 2x+y+2z=0 
# 2x-y+z=10 
# x+3y-z=5

A=np.array([[2,1,2],[2,-1,1],[1,3,-1]])
B=np.array([0,10,5])
X=np.linalg.solve(A,B)
print(X)