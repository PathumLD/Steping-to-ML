# Truthy/Falsy conversions
print(bool(1))     # True
print(bool(0))     # False
print(bool(""))    # False
print(bool("Hi"))  # True
print(bool([]))    # False
print(bool([1]))   # True

# Explicit boolean conversion
num = 10
if bool(num):
    print("Number is non-zero")