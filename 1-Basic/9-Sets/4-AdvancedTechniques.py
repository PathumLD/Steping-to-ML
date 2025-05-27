# Deduplication
names = ['Alice', 'Bob', 'Alice', 'Charlie']
unique_names = list(set(names))  # Order not preserved!

# Set comprehensions
squares = {x**2 for x in range(10)}
even_squares = {x**2 for x in range(10) if x % 2 == 0}

# Frozen sets (immutable)
constants = frozenset(['pi', 'e', 'c'])
# constants.add('G')  # AttributeError

# Dictionary view objects
d = {'a': 1, 'b': 2}
keys_set = d.keys()  # Set-like view