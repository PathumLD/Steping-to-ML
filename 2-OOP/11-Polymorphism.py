"""
Different classes can have methods with the same name, and the correct one is used depending on the object.

Polymorphism means "many forms." 
In OOP, it refers to the ability of different classes to be treated as instances of the same class through inheritance.
It allows you to define methods in the child class with the same name as in the parent class.
"""



class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Woof"

animals = [Cat(), Dog()]
for animal in animals:
    print(animal.speak())
