"""

Fundamental Concepts of Sets

Sets are unordered collections of unique, immutable objects that provide:

    Uniqueness: No duplicate elements allowed

    Membership Testing: Optimized for in operations

    Mathematical Operations: Union, intersection, difference

    Mutable/Immutable Variants: set (mutable) and frozenset (immutable)

Internal Implementation

1. Hash Table Structure:

    Uses hash tables for O(1) average case lookups

    Elements must be hashable (implement __hash__)

    Automatically handles hash collisions

2. Memory Allocation:

    Similar to dictionaries but only stores keys

    Starts with 8 slots, resizes when 2/3 full

    Resizing follows approximate 4x growth until 50K elements

Performance Characteristics

-------------|----------------------|-----------------------------|
Operation    | Time Complexity      | Explanation                 |
-------------|----------------------|-----------------------------|
Index Access | O(1)                 | Direct pointer arithmetic   |
-------------|----------------------|-----------------------------|
Append       | O(1) amortized       | Occasional resize needed    |
-------------|----------------------|-----------------------------|
Insert       | O(n)                 | Requires shifting elements  |
-------------|----------------------|-----------------------------|
Delete       | O(n)                 | Requires shifting elements  |
-------------|----------------------|-----------------------------|
Search       | O(n)                 | Linear scan required        |
-------------|----------------------|-----------------------------|
Slice        | O(k)                 | k = slice size              |
-------------|----------------------|-----------------------------|


Best Practices
    Use sets for membership testing and deduplication

    Prefer set operations over manual loops

    Convert to lists only when ordering needed

    Use frozen sets as dictionary keys

    Consider collections.Counter for multiset operations

    Use set comprehensions for readable transformations


Practical Exercises

1. Implement a spell checker that:

    Loads dictionary words into a set

    Checks text against dictionary

    Suggests corrections using set operations

2. Create a similarity analyzer that:

    Computes Jaccard similarity between documents

    Uses set intersection/union

    Handles large text files efficiently

3. Build a data processing pipeline that:

    Removes duplicate records

    Identifies unique/overlapping values across datasets

    Visualizes set relationships

4. Develop a custom set class that:

    Tracks insertion order

    Maintains statistics on operations

    Implements additional set relations    

"""