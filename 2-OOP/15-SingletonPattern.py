"""
The Singleton pattern ensures that a class has only one instance and provides a global point of access to that instance.
"""



class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance



class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            print("Creating new instance")
            cls._instance = super(Singleton, cls).__new__(cls)
            # Initialize any attributes here
            cls._instance.value = 0
        return cls._instance

# Usage
s1 = Singleton()
print(f"s1 value: {s1.value}")  # s1 value: 0

s1.value = 42
print(f"s1 value updated: {s1.value}")  # s1 value updated: 42

# Creating another "instance"
s2 = Singleton()  # No creation message
print(f"s2 value: {s2.value}")  # s2 value: 42 (same instance)

# Verify they're the same object
print(s1 is s2)  # True