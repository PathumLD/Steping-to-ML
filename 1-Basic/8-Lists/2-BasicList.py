# Creation
numbers = [1, 2, 3, 4]
mixed = [1, "two", 3.0, [4, 5]]

# Indexing
print(numbers[0])    # 1 (first element)
print(numbers[-1])   # 4 (last element)

# Slicing
print(numbers[1:3])  # [2, 3] (elements 1-2)
print(numbers[::2])  # [1, 3] (every other element)

# Modification
numbers[1] = 20      # [1, 20, 3, 4]
numbers.append(5)    # [1, 20, 3, 4, 5]
numbers.insert(1, 1.5) # [1, 1.5, 20, 3, 4, 5]