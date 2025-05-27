# Basic if statement
age = 20
if age >= 18:
    print("You are an adult")  # This will execute if age is 18 or more

# if-else statement
temperature = 15
if temperature > 25:
    print("It's warm outside")
else:
    print("It's cool outside")  # This will execute as temperature is 15

# if-elif-else chain
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"  # This will be assigned as score is 85
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Your grade is {grade}")  # Outputs: Your grade is B

# Nested conditionals
has_license = True
age = 20

if age >= 18:
    print("Age requirement met")  # This will execute as age is 20
    
    if has_license:
        print("You can drive")  # This will execute as has_license is True
    else:
        print("You need to get a license first")
else:
    print("You must be at least 18 years old to drive")

# Conditional expression (ternary operator)
age = 20
status = "adult" if age >= 18 else "minor"
print(status)  # Outputs: adult

# Using logical operators
has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit:
    print("Eligible for loan")  # This will execute as both conditions are True

if has_high_income or has_good_credit:
    print("At least one financial criterion met")  # This will execute

if not has_criminal_record:
    print("No criminal record")  # This will execute as not False is True

# Short-circuit evaluation
x = 5
y = 0
if x > 0 and y != 0 and x/y > 2:
    print("Condition met")
else:
    print("Condition not met")  # This will execute without error because Python
                                # short-circuits after evaluating y != 0 as False

# Checking multiple conditions with 'in' operator
fruit = "apple"
if fruit in ["apple", "banana", "cherry"]:
    print(f"{fruit} is in the list")  # This will execute

# Empty collections evaluation
items = []
if items:
    print("List has items")
else:
    print("List is empty")  # This will execute as empty list is falsy

# Checking identity with 'is' operator
x = None
if x is None:
    print("x is None")  # This will execute as x is None

# Common pattern: checking for None or providing default
def get_value(data, key, default=None):
    if key in data:
        return data[key]
    else:
        return default

user = {"name": "John", "age": 30}
email = get_value(user, "email", "No email provided")
print(email)  # Outputs: No email provided

# Chaining comparison operators
age = 25
if 18 <= age < 65:
    print("Working age")  # This will execute as 18 <= 25 < 65 is True





"""

Practical Exercises
1. Write a program that:

    Takes a number input

    Prints whether it's positive, negative, or zero

    Checks if it's even or odd

2. Create a login system that:

    Checks username length (> 3 chars)

    Verifies password meets complexity requirements

    Gives appropriate feedback

3. Implement a temperature converter with conditions:

    Ask user for conversion direction (C→F or F→C)

    Validate input ranges

    Provide appropriate output

4. Write a function that:

    Takes three numbers

    Returns the largest using only conditional statements

    Handles equal values appropriately

"""