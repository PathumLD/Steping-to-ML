"""
Classes are blueprints for creating objects.
They define attributes (data) and methods (functions) that the objects created from the class will have.
Objects are instances of a class - concrete entities based on the class blueprint.
"""


# Defining a simple class
class Dog:
    # Class attributes/variables (shared by all instances)
    species = "Canis familiaris"
    
    # Methods
    def bark(self):
        return "Woof!"

# Creating objects (instances)
my_dog = Dog()  # Instantiating a Dog object
print(my_dog.species)  # Accessing an attribute
print(my_dog.bark())   # Calling a method