"""
Magic methods (double underscore methods or dunder methods) are special methods that start and end with double underscores.
They enable operator overloading and other behaviors.
"""


# 1.1 __str__ and __repr__

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r})"

b = Book("1984", "George Orwell")
print(str(b))   # 1984 by George Orwell
print(repr(b))  # Book('1984', 'George Orwell')



# 1.2 Operator Overloading

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)        # (4, 6)
print(p1 == p2)       # False




# 1.3 Container-Like Behavior (__getitem__, __len__)

class MyList:
    def __init__(self, items):
        self._items = items

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

ml = MyList([10, 20, 30])
print(ml[1])    # 20
print(len(ml))  # 3





class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # String representation
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    # Official representation (for debugging)
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    # Addition operator overloading
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    # Subtraction operator overloading
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    # Equality comparison
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    # Length method (magnitude of vector)
    def __len__(self):
        import math
        return int(math.sqrt(self.x**2 + self.y**2))
    
    # GetItem to allow indexing
    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")

# Create vectors
v1 = Vector(3, 4)
v2 = Vector(5, 6)

# Test magic methods
print(v1)                # Vector(3, 4) - __str__
print(repr(v2))          # Vector(5, 6) - __repr__
print(v1 + v2)           # Vector(8, 10) - __add__
print(v2 - v1)           # Vector(2, 2) - __sub__
print(v1 == Vector(3, 4))  # True - __eq__
print(len(v1))           # 5 - __len__ (magnitude of vector)
print(v1[0], v1[1])      # 3 4 - __getitem__