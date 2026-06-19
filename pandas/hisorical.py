import matplotlib.pyplot as plt 
import numpy as np 

x = np.random.normal(170, 30, 200)

plt.hist(x)
plt.show()