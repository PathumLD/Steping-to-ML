"""

What is Typecasting?
    Typecasting (or type conversion) is the process of converting one data type to another. Python supports both implicit and explicit type conversion.

Types of Type Conversion:
1. Implicit Conversion:

    Automatically performed by Python interpreter

    Occurs when mixing compatible types (e.g., int + float → float)

    No data loss in safe conversions

2. Explicit Conversion:

    Manually performed using constructor functions

    Required when there might be data loss or incompatibility

    Examples: int(), float(), str(), list(), etc.

Conversion Hierarchy:
Python follows a hierarchy for implicit conversions:
bool → int → float → complex

Important Considerations:
    Not all types can be converted to all other types

    Some conversions may lose precision (float → int)

    Some conversions may raise exceptions if invalid


Practical Exercises
1. Create a program that:

    Takes numeric input as string

    Converts to appropriate numeric type

    Performs calculations

    Converts back to string for display

2. Write a function that:

    Accepts mixed type list (numbers as strings and actual numbers)

    Returns list with all elements converted to floats

    Handles invalid entries gracefully

3. Implement a type checker/converter that:

    Identifies input type

    Suggests possible conversions

    Performs requested conversion with validation

4. Experiment with:

    Converting between different collection types

    Custom object to string conversion using __str__

    Binary/hexadecimal conversions of numbers  

"""