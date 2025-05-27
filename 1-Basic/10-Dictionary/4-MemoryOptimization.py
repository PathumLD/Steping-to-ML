import sys

# Size comparison
empty = {}
small = {'a': 1}
large = {x: x for x in range(1000)}

print(sys.getsizeof(empty))  # ~64 bytes (overhead)
print(sys.getsizeof(small))  # ~232 bytes
print(sys.getsizeof(large))  # ~36968 bytes

# Space-saving with __slots__
class Point:
    __slots__ = ['x', 'y']  # Fixed attributes
    def __init__(self, x, y):
        self.x = x
        self.y = y

# More memory efficient than regular class with __dict__