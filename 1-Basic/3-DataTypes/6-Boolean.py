is_active = True
has_permission = False

print(is_active, type(is_active))  # Outputs: True <class 'bool'>

# Boolean operations
print(not is_active)             # Logical NOT: False
print(is_active and has_permission)  # Logical AND: False
print(is_active or has_permission)   # Logical OR: True

# Boolean conversion
print(bool(0))      # Falsy value: False
print(bool(42))     # Truthy value: True
print(bool(""))     # Empty string (Falsy): False
print(bool("hello"))  # Non-empty string (Truthy): True
print(bool([]))     # Empty list (Falsy): False
print(bool([1, 2]))  # Non-empty list (Truthy): True