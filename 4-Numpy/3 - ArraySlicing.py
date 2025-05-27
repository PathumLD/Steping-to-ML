import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9])
print(a)

#print(start:end)
print(a[1:5])
print(a[:4])
print(a[6:])

#print(start:end:step)
print(a[1:7:2])
print(a[1::2])


b = np.array([[1,2,3], [4,5,6]])

print(b[0,1:])
print(b[:3])
print(b[1:])