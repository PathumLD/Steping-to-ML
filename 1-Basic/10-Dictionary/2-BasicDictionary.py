# Creation
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
empty_dict = {}  # or dict()

# Access
print(person['name'])        # Alice
print(person.get('country', 'USA'))  # USA (default)

# Modification
person['age'] = 31          # Update
person['country'] = 'USA'   # Add new
del person['city']          # Remove

# Iteration
for key in person:          # Keys
    print(key)

for key, value in person.items():  # Items
    print(f"{key}: {value}")

# Dictionary views
keys = person.keys()        # Dynamic view
values = person.values()    # Updates with dict