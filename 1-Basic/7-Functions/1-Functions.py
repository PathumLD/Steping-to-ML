"""

Functions are reusable blocks of code that:

    1. Encapsulate logic into named units

    2. Accept parameters (inputs)

    3. Return values (outputs)

    4. Promote code reuse and modularity

Function Components
1. Definition:

python

        def function_name(parameters):
            # docstring
            # function body
            return value

2. Parameters vs Arguments:

    Parameters: Variables listed in function definition

    Arguments: Actual values passed during function call

3. Namespaces and Scope:

    Local scope: Variables defined inside function

    Enclosing scope: For nested functions

    Global scope: Module-level variables

    Built-in scope: Python's built-in names

Advanced Function Features
1. First-class Objects:

    Can be assigned to variables

    Can be passed as arguments

    Can be returned from other functions

2. Closures:

    Functions that remember values in enclosing scope

    Created when nested functions reference non-local variables

3. Decorators:

    Functions that modify behavior of other functions

    Use @decorator syntax



    Best Practices

1. Single Responsibility Principle:

    Each function should do one thing well

2. Naming Conventions:

    Use lowercase with underscores

    Choose descriptive names

    Verbs for actions, nouns for data retrievers

3. Parameter Design:

    Order: Required → Default → *args → **kwargs

    Avoid mutable default arguments

4. Documentation:

    Always include docstrings

    Document parameters and return values


Practical Exercises
1. Create a function that:

    Takes a list of numbers

    Returns statistics (min, max, average, median)

    Handles empty lists gracefully

2. Implement a password validator:

    Checks length requirements

    Verifies character diversity

    Returns detailed validation results

3. Build a decorator that:

    Times function execution

    Logs results to a file

    Works with any function

4. Write a closure-based counter:

    Starts at given initial value

    Returns increment/decrement functions

    Maintains internal state    

"""