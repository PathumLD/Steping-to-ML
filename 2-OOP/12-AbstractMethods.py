"""
Abstract methods are methods that are declared but contain no implementation.
They must be implemented by derived classes.
In Python, abstract methods are created using the abc module.
"""


from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"



from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass
    
    def honk(self):
        return "Beep beep!"

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"
    
    def stop_engine(self):
        return "Car engine stopped"

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started"
    
    def stop_engine(self):
        return "Motorcycle engine stopped"
    
    # Override the non-abstract method
    def honk(self):
        return "Motorcycle horn: Beep!"

# Creating instances
# vehicle = Vehicle()  # TypeError: Can't instantiate abstract class
car = Car()
motorcycle = Motorcycle()

print(car.start_engine())       # Car engine started
print(motorcycle.start_engine())  # Motorcycle engine started
print(car.honk())               # Beep beep!
print(motorcycle.honk())        # Motorcycle horn: Beep!