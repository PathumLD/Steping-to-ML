import numpy as np

# Integer           - i
# Boolean           - bool
# Float             - f
# Complex           - c
# Unicode String    - U
# Time Delta        - m
# Date Time         - M
# Object            - O

arr1 = np.array([1,2,3,4])
print(arr1)
print(arr1.dtype)

arr2 = np.array(["Pathum", "Lakshan", "dissanayake"])
print(arr2)
print(arr2.dtype)


arr3 = np.array([1,2,3,4], dtype='f')
print(arr3)
print(arr3.dtype)

arr4 = np.array([1,2,3,4])
print(arr4)
print(arr4.dtype)
arr5 = arr4.astype(bool)
print(arr5)
print(arr5.dtype)