import numpy as np

# Join 

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

newarr = np.concatenate((arr1,arr2))
print(newarr)
print('\n')


arr3 = np.array([[1, 2, 3], [4, 5, 6]])
arr4 = np.array([[4, 5, 6], [7, 8, 9]])

newarr2 = np.concatenate((arr3, arr4), axis=0)
print(newarr2)
print('\n')


# Split

arr5 = np.array([1,2,3,4,5,6,7,8,9])

newarr3 = np.array_split(arr5, 2)
print(newarr3)

arr6 = np.array([[1, 2, 3], [4, 5, 6]])

newarr4 = np.array_split(arr6, 2)
print(newarr4)