"""
Decorators provide a way to modify or enhance the behavior of classes or methods without changing their implementation.
They are functions that take another function as an argument and return a modified version.
"""


def log_method(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class MyService:
    @log_method
    def do_task(self):
        print("Task done.")



def log_calls(func):
    def wrapper(*args, **kwargs):
        class_name = args[0].__class__.__name__ if args else ""
        print(f"Calling {class_name}.{func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {class_name}.{func.__name__}")
        return result
    return wrapper

class Calculator:
    @log_calls
    def add(self, x, y):
        return x + y
    
    @log_calls
    def multiply(self, x, y):
        return x * y

# Class decorator
def add_greeting(cls):
    # Add a new method to the class
    cls.greet = lambda self: f"Hello from {self.__class__.__name__}"
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

# Using decorated methods
calc = Calculator()
print(calc.add(5, 3))       # Output shows log messages around result 8
print(calc.multiply(4, 7))  # Output shows log messages around result 28

# Using class with added method via decorator
person = Person("Alice")
print(person.get_name())  # Alice
print(person.greet())     # Hello from Person