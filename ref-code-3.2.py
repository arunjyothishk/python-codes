import numpy as np

# 2x+y+2z=0 
# 2x-y+z=10 
# x+3y-z=5

A=np.array([[5,-3],
            [17,21]])

B=np.array([-50 ,170])
X=np.linalg.solve(A,B)
print(X)