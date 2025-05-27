"""
The __init__ method is a special method that gets called when an object is created.
It initializes attributes of the object.
"""


class Student:
    def __init__(self, name, age, grade):
        # Initialize attributes
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

# Creating instance with initial values
alice = Student("Alice", 15, "10th")
print(alice.get_info())