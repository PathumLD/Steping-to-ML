# Integer
x = 10
print(type(x))  # <class 'int'>

# Float
y = 3.14
print(type(y))  # <class 'float'>

# Complex
z = 2 + 3j
print(type(z))  # <class 'complex'>
print(z.real)   # 2.0
print(z.imag)   # 3.0

# Type conversion
a = float(x)    # int to float
b = int(y)      # float to int (truncates)