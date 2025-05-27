A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union
print(A | B)       # {1, 2, 3, 4, 5, 6}
print(A.union(B))  # Same

# Intersection
print(A & B)             # {3, 4}
print(A.intersection(B)) # Same

# Difference
print(A - B)          # {1, 2}
print(A.difference(B)) # Same

# Symmetric Difference
print(A ^ B)                     # {1, 2, 5, 6}
print(A.symmetric_difference(B)) # Same

# Subset checks
print({1, 2} <= A)  # True (subset)
print(A.isdisjoint({7, 8}))  # True