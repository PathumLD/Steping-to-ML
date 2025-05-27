"""
Attributes are variables that belong to a class or object
Methods are functions that belong to a class or object and define their behaviors
"""


class Car:
    # Attributes
    color = "red"
    
    # Methods
    def drive(self):
        return "The car is moving!"
    
    def honk(self):
        return "Beep beep!"

my_car = Car()
print(my_car.color)      # Accessing attribute
print(my_car.drive())    # Calling method