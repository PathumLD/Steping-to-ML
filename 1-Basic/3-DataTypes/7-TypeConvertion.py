x = 10
print(float(x))     # int to float: 10.0
print(str(x))       # int to string: "10"
print(bool(x))      # int to bool: True

y = "123"
print(int(y))       # string to int: 123
print(float(y))     # string to float: 123.0

# Checking types
print(isinstance(x, int))      # Check if x is an integer: True
print(isinstance(y, str))      # Check if y is a string: True







# Type checking
print(type(42))           # Outputs: <class 'int'>
print(isinstance(42, int))  # Outputs: True

# Type conversion (casting)
# Converting between numeric types
num_int = 123
num_float = float(num_int)    # int to float: 123.0
num_complex = complex(num_int)  # int to complex: (123+0j)

# Converting to/from strings
num_str = "456"
num_int_from_str = int(num_str)  # string to int: 456
str_from_int = str(42)          # int to string: "42"

# List, tuple, set conversions
my_list = [1, 2, 3, 2]
print(tuple(my_list))   # list to tuple: (1, 2, 3, 2)
print(set(my_list))     # list to set: {1, 2, 3} (duplicates removed)

my_tuple = ('a', 'b', 'c')
print(list(my_tuple))   # tuple to list: ['a', 'b', 'c']

my_set = {4, 5, 6}
print(list(my_set))     # set to list: [4, 5, 6]