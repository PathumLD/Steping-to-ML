"""

Understanding Exceptions
Exceptions are events that disrupt normal program flow when errors occur. 
Python uses a hierarchical exception class structure where all exceptions inherit from BaseException.

Key Concepts:
1. Exception Hierarchy:


    BaseException
    ├── SystemExit
    ├── KeyboardInterrupt
    ├── GeneratorExit
    └── Exception
        ├── ArithmeticError
        │    ├── ZeroDivisionError
        │    └── FloatingPointError
        ├── LookupError
        │    ├── IndexError
        │    └── KeyError
        ├── OSError
        │    ├── FileNotFoundError
        │    └── PermissionError
        └── many more...


2. Exception Handling Flow:

    When exception occurs, Python creates exception object

    Normal execution stops and interpreter searches for handler

    If no handler found, program terminates with traceback

3. Common Built-in Exceptions:

    ValueError: Invalid value

    TypeError: Invalid operation for type

    IndexError: Sequence index out of range

    KeyError: Dictionary key not found

    AttributeError: Attribute reference fails

    ImportError: Module import fails

    
Practical Exercises
1. Create a file processor that:

    Handles missing files gracefully

    Validates file contents

    Provides meaningful error messages

2. Implement a calculator that:

    Catches invalid numeric input

    Handles division by zero

    Reports all errors clearly

3. Write a function that:

    Takes a dictionary and key

    Safely accesses nested dictionaries

    Raises custom exception for invalid paths

4. Build a custom exception hierarchy for:

    User authentication errors

    Database operation errors

    Network communication errors

"""