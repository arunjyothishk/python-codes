import numpy as np
import matplotlib.pyplot as plt
from numpy import random
M=10
x = np.arange(0, M, 1)
y=random.randint(11, size=(M))
plt.boxplot(y)
plt.title("Box plot")

plt.show()
print(y)