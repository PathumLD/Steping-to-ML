import numpy as np

# 1D Array

arr1 = np.array([1, 2, 3, 4, 5])

for i in arr1:
    print(i)
print('\n')



# 2D Array

arr2 = np.array([[1,2,3], [4,5,6]])

for i in arr2:
    for j in i:
        print(j)
print('\n')


# Any Dimention Array (nditer)

arr3 = np.array([[[1,2],[3,4]],[[5,6], [7,8]]])

for i in np.nditer(arr3):  # ---> for i in np.nditer(arr3[start:end:step])
    print(i)
print('\n')


# By using nditer we can iterate any dimention of array easily instead of using nested for loops


# Get index of the value

arr4 = np.array([[1,2,3], [4,5,6], [7,8,9]])

for i,j in np.ndenumerate(arr4):
    print(i,j)


arr5 = np.array([[[1,2],[3,4]],[[5,6], [7,8]]])

for i,j in np.ndenumerate(arr5):
    print(i,j)


# In here i and j is used to output index and value