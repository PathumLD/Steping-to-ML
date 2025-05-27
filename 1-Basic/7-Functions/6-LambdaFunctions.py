square = lambda x: x ** 2
print(square(5))  # 25

# Typical use with higher-order functions
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16]