import numpy as np 

a = np.array([1,2,3])
print(a[2] + a[1])

b = np.array([[1,2,3],[4,5,6]])
print(b)

c =  np.array([[1,2,3],[4,5,6],[7,8,9]])
print(c)
print(a.ndim)
print(b.ndim)
print(c.ndim)



import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::-1])
print