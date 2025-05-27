"""
The Factory pattern provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created.
"""


class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_factory(animal_type):
    if animal_type == "dog":
        return Dog()
    elif animal_type == "cat":
        return Cat()




class Animal:
    def speak(self):
        pass
    
    def __str__(self):
        return self.__class__.__name__

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

# Factory class
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        elif animal_type.lower() == "cow":
            return Cow()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Client code
factory = AnimalFactory()

# Create different animals using the factory
animals = [
    factory.create_animal("dog"),
    factory.create_animal("cat"),
    factory.create_animal("cow")
]

# Make them speak
for animal in animals:
    print(f"{animal} says: {animal.speak()}")