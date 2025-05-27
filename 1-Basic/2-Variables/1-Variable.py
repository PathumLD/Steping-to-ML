# Basic variable assignment
name = "John"
age = 30
height = 5.9
is_student = True

# Printing variables
print(name)  # Outputs: John
print(age)   # Outputs: 30

# Checking variable types
print(type(name))      # Outputs: <class 'str'>
print(type(age))       # Outputs: <class 'int'>
print(type(height))    # Outputs: <class 'float'>
print(type(is_student)) # Outputs: <class 'bool'>

# Reassigning variables (dynamic typing)
x = 10          # x is an integer
print(x)        # Outputs: 10
x = "Hello"     # Now x is a string
print(x)        # Outputs: Hello

# Multiple assignment
a, b, c = 5, 3.2, "Hello"
print(a, b, c)  # Outputs: 5 3.2 Hello

# Swapping variables
a, b = 1, 2
print(a, b)  # Outputs: 1 2
a, b = b, a  # Swap values
print(a, b)  # Outputs: 2 1

# Variable scope example
def my_function():
    local_var = "I am local"  # Local scope
    print(local_var)
    print(global_var)         # Accessing global variable

global_var = "I am global"    # Global scope
my_function()                 # Outputs: I am local
                              #          I am global

# Modifying global variables inside functions
def modify_global():
    global global_var  # Declare use of global variable
    global_var = "I've been modified"

print(global_var)      # Outputs: I am global
modify_global()
print(global_var)      # Outputs: I've been modified

# Deleting variables
del global_var
# print(global_var)    # This would raise an error (NameError) since the variable no longer exists



"""

Practical Exercise
1. Create variables to store:

    Your name

    Your age

    Your height in meters

    Whether you're a student (True/False)

2. Print all variables with descriptive messages

3. Create a function that:

    Takes two numbers as parameters

    Uses local variables for calculations

    Returns the sum and product

4. Demonstrate variable swapping

"""