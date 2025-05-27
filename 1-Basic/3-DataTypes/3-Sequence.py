# String
greeting = "Hello, Python!"
name = 'Alice'

print(greeting, type(greeting))  # Outputs: Hello, Python! <class 'str'>

# String operations
print(len(greeting))             # Length: 14
print(greeting[0])               # First character: H
print(greeting[-1])              # Last character: !
print(greeting[7:13])            # Slicing: Python
print(greeting + " " + name)     # Concatenation: Hello, Python! Alice
print("Hello" * 3)               # Repetition: HelloHelloHello
print("Python" in greeting)      # Membership test: True



# List
fruits = ["apple", "banana", "cherry"]
mixed_list = [1, "hello", 3.14, True]

print(fruits, type(fruits))      # Outputs: ['apple', 'banana', 'cherry'] <class 'list'>

# List operations
fruits.append("orange")           # Add an item
fruits.insert(1, "blueberry")     # Insert at position
fruits.remove("banana")           # Remove by value
popped_fruit = fruits.pop()       # Remove & return last item
print(fruits)                     # Outputs: ['apple', 'blueberry', 'cherry']
print(popped_fruit)               # Outputs: orange
print(len(fruits))                # Length: 3
print(fruits[0])                  # First item: apple
print(fruits[-1])                 # Last item: cherry
print(fruits[1:])                 # Slicing: ['blueberry', 'cherry']



# Tuple
coordinates = (10, 20)
mixed_tuple = (1, "hello", 3.14)
single_item_tuple = (42,)  # Note the comma

print(coordinates, type(coordinates))  # Outputs: (10, 20) <class 'tuple'>

# Tuple operations (note: tuples are immutable)
print(len(coordinates))          # Length: 2
print(coordinates[0])            # First item: 10
print(coordinates + (30, 40))    # Concatenation: (10, 20, 30, 40)
print((1, 2) * 3)                # Repetition: (1, 2, 1, 2, 1, 2)
# tup[1] = 3.14 # Error - immutable