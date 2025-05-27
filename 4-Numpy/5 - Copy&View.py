import numpy as np

# Copy

#In here when we use copy the connection with the original array is disconnected

x = np.array([1, 2, 3, 4, 5])
y = x.copy()

x[0] = 9

print(x) # -> [9 2 3 4 5]
print(y) # -> [1 2 3 4 5]



# View

# In here b gets a copy of a but they are connected each other

a = np.array([1, 2, 3, 4, 5])
b = a.view()

a[0] = 9

print(a) # -> [9 2 3 4 5]
print(b) # -> [9 2 3 4 5]



# to print original data
print(x.base) # Use base