import numpy as np

# Shape

arr1 = np.array([[1,2,3,4], [5,6,7,8]])

print(arr1)
print(arr1.shape)
print('\n')


arr2 = np.array([[[1,2,3],[3,4,5]],[[5,6,7], [7,8,9]]])

print(arr2)
print(arr2.shape)
print('\n')


# Reshape

arr3 = np.array([1,2,3,4,5,6,7,8,9])

arr4 = arr3.reshape(3,3)
print(arr4)
print('\n')


arr5 = np.array([1,2,3,4,5,6,7,8])

arr6 = arr5.reshape(2,2,2)
print(arr6)
print('\n')


# In here we have some conditions

#   1. New array shape (x,y) multiplication equals to the no of elemets
#   2. Otherwise you will get an error
#   3. You can use -1 if you don't know the exact one value. in 3D array other 2 numbers must know.


arr7 = np.array([1,2,3,4,5,6,7,8])

arr8 = arr7.reshape(2,2,-1)
print(arr8)
print('\n')

# If you want to display any dimention array as 1D array 

arr9 = np.array([[1,2,3,4], [5,6,7,8]])

arr10 = arr9.reshape(-1)
print(arr10)
print('\n')