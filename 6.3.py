import numpy as np 
import matplotlib.pyplot as plt
# dataset1
x1 =np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9])  
y1 =np.array([99, 86, 87, 88, 100, 86, 103, 87, 94, 78, 77, 85]) 
# dataset2 
x2 =np.array([26, 29, 48, 64, 6, 5, 36, 66, 55, 40])   
y2 =np.array([26, 34, 90, 33, 38, 20, 56, 2, 70, 15]) 
plt.scatter(x1, y1, c ="blue")   
plt.scatter(x2,y2,c="red")
plt.title('Scatter plot')
plt.show()