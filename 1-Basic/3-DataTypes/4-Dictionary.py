person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(person, type(person))      # Outputs: {'name': 'John', 'age': 30, 'city': 'New York'} <class 'dict'>

# Dictionary operations
print(person["name"])            # Access by key: John
person["email"] = "john@example.com"  # Add new key-value pair
person["age"] = 31               # Modify existing value
print(person.keys())             # All keys: dict_keys(['name', 'age', 'city', 'email'])
print(person.values())           # All values: dict_values(['John', 31, 'New York', 'john@example.com'])
print(person.items())            # All key-value pairs
print("name" in person)          # Key existence check: True
del person["city"]               # Remove a key-value pair
print(person)                    # Outputs: {'name': 'John', 'age': 31, 'email': 'john@example.com'}