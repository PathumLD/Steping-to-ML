import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])

x = np.where(arr == 3)
print(arr)
print(x)
print('\n')


arr1 = np.array([[1,2,3,4], [5,6,7,8]])

y = np.where(arr1 == 3)
print(arr1)
print(y)
print('\n')


# Find even numbers

arr2 = np.array([1,2,3,4,5,6,7,8,9])

z = np.where(arr2 % 2 ==0)
print(arr2)
print(z)
print('\n')


# searchsorted()  used only for sorted arrays

arr3 = np.array([1,3,5,7,9])

a = np.searchsorted(arr3 , 3)
b = np.searchsorted(arr3 , 3, side = 'right')
print(arr3)
print(a)
print(b)
print('\n')


c = np.searchsorted(arr3 , [4,6,7,8])
print(arr3)
print(c)
print('\n')