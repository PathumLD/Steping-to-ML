import numpy as np

#1D Array
x = np.array([1,2,3,4], ndmin = 2)
print('This is 1D Array')
print(x)
print("Dimension is : ",x.ndim)
print("\n")



#2D Array
y = np.array([[1,2,3], [4,5,6]], ndmin = 3)
print('This is 2D Array')
print(y)
print("Dimension is : ",y.ndim)
print("\n")


#3D Array
z = np.array([[[1,2], [3,4]], [[5,6], [7,8]]], ndmin = 4)
print('This is 3D Array')
print(z)
print("Dimension is : ",z.ndim)
print("\n")