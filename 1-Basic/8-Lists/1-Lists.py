"""

Lists are ordered, mutable sequences that form one of Python's most versatile data structures. They are:

    Ordered: Elements maintain their position

    Mutable: Contents can be changed after creation

    Heterogeneous: Can contain different data types

    Dynamic: Automatically resize as needed

Memory Architecture
1. Internal Representation:

    Implemented as dynamic arrays

    Pre-allocate extra space for growth (amortized O(1) appends)

    When capacity exceeded, Python allocates new larger array (typically ~1.125x growth)

2. Element Storage:

    Stores references to objects (not objects themselves)

    Each element is a pointer to the actual data

Performance Characteristics

-------------|----------------------|-----------------------------|
Operation	 |   Time Complexity	|       Explanation           |
-------------|----------------------|-----------------------------|
Index Access |	 O(1)	            |   Direct pointer arithmetic |
-------------|----------------------|-----------------------------|
Append	     |   O(1) amortized	    |   Occasional resize needed  |
-------------|----------------------|-----------------------------|
Insert	     |   O(n)	            |   Requires shifting elements|
-------------|----------------------|-----------------------------|
Delete	     |   O(n)	            |   Requires shifting elements|
-------------|----------------------|-----------------------------|
Search	     |   O(n)	            |   Linear scan required      |
-------------|----------------------|-----------------------------|
Slice	     |   O(k)	            |   k = slice size            |
-------------|----------------------|-----------------------------|



Best Practices

    Use list comprehensions for transformations

    Prefer append/extend over + for large lists

    Consider collections.deque for frequent insertions at both ends

    Use enumerate when index needed during iteration

    Sort with key parameter for complex sorting

    Consider generators for memory efficiency with large data

    
Practical Exercises
1. Implement a function that:

    Takes a list of numbers

    Returns new list with running average

    Handles edge cases (empty list, etc.)

2. Create a matrix operations module with:

    Matrix transposition using nested lists

    Matrix multiplication

    Determinant calculation (for small matrices)

3. Write a function that:

    Flattens arbitrarily nested lists

    Preserves order

    Handles non-list elements gracefully

4. Benchmark different approaches:

    List comprehension vs manual append

    Various copying methods

    Sorting techniques

"""