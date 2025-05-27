lst = [3, 1, 4, 1, 5, 9]

# Add elements
lst.append(2)         # [3, 1, 4, 1, 5, 9, 2]
lst.extend([5, 3])     # [3, 1, 4, 1, 5, 9, 2, 5, 3]
lst += [5, 8]          # Alternative extend

# Remove elements
lst.remove(1)          # Removes first 1
popped = lst.pop(3)    # Removes and returns element at index 3
del lst[2:4]           # Removes slice

# Information
count = lst.count(5)   # Count occurrences
index = lst.index(9)   # Find first index
lst.sort()             # In-place sort
lst.reverse()          # In-place reverse

# Memory operations
copy = lst.copy()      # Shallow copy
lst.clear()            # Empty the list