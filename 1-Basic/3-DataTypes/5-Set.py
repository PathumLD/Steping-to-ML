unique_numbers = {1, 2, 3, 4, 5}
duplicate_set = {1, 2, 2, 3, 4, 4, 5}  # Duplicates are automatically removed

print(unique_numbers, type(unique_numbers))  # Outputs: {1, 2, 3, 4, 5} <class 'set'>
print(duplicate_set)             # Outputs: {1, 2, 3, 4, 5}

# Set operations
unique_numbers.add(6)            # Add an element
unique_numbers.remove(2)         # Remove an element
print(unique_numbers)            # Outputs: {1, 3, 4, 5, 6}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))          # Union: {1, 2, 3, 4, 5}
print(set1.intersection(set2))   # Intersection: {3}
print(set1.difference(set2))     # Difference: {1, 2}