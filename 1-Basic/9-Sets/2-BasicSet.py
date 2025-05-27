# Creation
colors = {'red', 'green', 'blue'}
empty_set = set()  # {} creates dict!

# Adding elements
colors.add('yellow')
colors.update(['orange', 'purple']) 

# Removing elements
colors.remove('green')  # Raises KeyError if missing
colors.discard('pink')  # No error
popped = colors.pop()   # Removes arbitrary element

# Membership testing
if 'red' in colors:
    print("Red is present")