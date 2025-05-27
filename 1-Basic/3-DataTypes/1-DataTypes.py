"""

1. Numeric Types:

    int: Integer numbers (e.g., 5, -17, 0)
    float: Floating-point numbers (e.g., 3.14, -2.5, 0.0)
    complex: Complex numbers (e.g., 2+3j, -1j)


2. Sequence Types:

    str: String of characters (e.g., "hello", 'Python')
    list: Ordered, mutable collection (e.g., [1, 2, 3])
    tuple: Ordered, immutable collection (e.g., (1, 2, 3))


3. Mapping Type:

    dict: Key-value pairs (e.g., {'name': 'John', 'age': 30})


4. Set Types:

    set: Unordered collection of unique items (e.g., {1, 2, 3})
    frozenset: Immutable version of set


5. Boolean Type:

    bool: True or False values


6. Binary Types:

    bytes: Immutable sequence of bytes
    bytearray: Mutable sequence of bytes
    memoryview: Memory view of bytes-like object



Type Characteristics
Each data type has specific properties and behaviors:

    * Mutability: Can the object be changed after creation?

        Mutable types: list, dict, set, bytearray
        Immutable types: int, float, complex, str, tuple, frozenset, bytes


    * Ordered vs Unordered: Can elements be accessed by position?

        Ordered types: str, list, tuple
        Unordered types: set, frozenset, dict (though dict preserves insertion order since Python 3.7)

        
Practical Exercises
1. Create variables representing:

    Your age (integer)

    Your exact weight (float)

    Your name (string)

    Your hobbies (list)

    Your personal details (dictionary)

2. Perform operations:

    Convert between numeric types

    Slice strings and lists

    Add/remove items from lists and dictionaries

    Demonstrate set operations

3. Experiment with:

    Tuple packing/unpacking

    Boolean evaluations

    Type checking with isinstance()

"""