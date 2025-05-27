# Implicit conversion
x = 5    # int
y = 2.5  # float
result = x + y  # result becomes float (7.5)
print(type(result))  # <class 'float'>

# Explicit conversion
a = "123"
num = int(a)  # string to int
print(num * 2)  # 246

pi = 3.14159
int_pi = int(pi)  # float to int (truncates)
print(int_pi)  # 3