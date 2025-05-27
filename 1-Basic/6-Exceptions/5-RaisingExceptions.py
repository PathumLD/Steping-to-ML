def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 120:
        raise ValueError("Age seems unrealistic")
    return True

try:
    validate_age(-5)
except ValueError as ve:
    print(f"Invalid age: {ve}")