"""
Inheritance is a mechanism that allows a class to inherit attributes and methods from another class.
The original class is the parent/base/super class, and the derived class is the child/derived/sub class.
"""


class phone1:
    def feature1(self):
        print("Bluetooth")

class phone2(phone1):
    def feature2(self):
        print("Camera")

class phone3(phone2):
    def feature3(self):
        print("Internet")
    


myobj = phone1()   #Single Inheritance
myobj.feature1()



class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic animal sound"
    
    def info(self):
        return f"{self.name} is a {self.species}"

# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # Initialize the parent class
        super().__init__(name, species="Dog")
        self.breed = breed
    
    # Method overriding
    def make_sound(self):
        return "Woof!"
    
    # Additional method
    def wag_tail(self):
        return f"{self.name} wags tail happily"

# Creating instances
generic_animal = Animal("Generic", "Unknown")
my_dog = Dog("Rex", "German Shepherd")

print(generic_animal.info())          # Generic is a Unknown
print(generic_animal.make_sound())    # Some generic animal sound

print(my_dog.info())                  # Rex is a Dog
print(my_dog.make_sound())            # Woof!
print(my_dog.wag_tail())              # Rex wags tail happily




# The Super() Function

"""
Used to call methods from the parent class.
"""

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # call parent constructor
        self.breed = breed


# Method Overriding

"""
Child class can provide a different implementation of a method already defined in its parent class.
"""


class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # call parent constructor
        self.breed = breed


class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")



class Shape:
    def area(self):
        return "Area calculation not implemented for generic shape"
    
    def perimeter(self):
        return "Perimeter calculation not implemented for generic shape"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    # Override area method
    def area(self):
        return self.width * self.height
    
    # Override perimeter method
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    # Override area method
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    # Override perimeter method
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

# Create shapes
rect = Rectangle(5, 10)
circle = Circle(7)

# Polymorphism in action
shapes = [rect, circle]
for shape in shapes:
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


#IF YOU NEED TO DISPLAY VALUES
class Fruit:
    number_of_items = None
    unit_price = None
    def setValue(self, x, y):
        self.number_of_items = x
        self.unit_price = y

class Apple(Fruit):
    def price(self):
        print('For Apple ', self.number_of_items * self.unit_price)

class Orange(Fruit):
    def price(self):
        print("For Orange ", self.number_of_items * self.unit_price)

class Mango(Fruit):
    def price(self):
        print("For Mango ", self.number_of_items * self.unit_price)

myObj1 = Apple()
myObj2 = Orange()  # Fixed: Changed myobj2 (lowercase 'o') to myObj2
myObj3 = Mango()

myObj1.setValue(10, 30)
myObj2.setValue(10, 30)
myObj3.setValue(10, 30)

# Call the price methods to see the output
myObj1.price()
myObj2.price()
myObj3.price()



# IF YOU NEED TO RETURN A VALUE
class Fruit:
    number_of_items = None
    unit_price = None
    def setValue(self, x, y):
        self.number_of_items = x
        self.unit_price = y

class Apple(Fruit):
    def price(self):
        result = self.number_of_items * self.unit_price
        print('For Apple ', result)
        return result  # Return the value

class Orange(Fruit):
    def price(self):
        result = self.number_of_items * self.unit_price
        print("For Orange ", result)
        return result  # Return the value

class Mango(Fruit):
    def price(self):
        result = self.number_of_items * self.unit_price
        print("For Mango ", result)
        return result  # Return the value

myObj1 = Apple()
myObj2 = Orange()
myObj3 = Mango()


myObj1.setValue(10, 30)
myObj2.setValue(15, 35)
myObj3.setValue(12, 40)

Total = myObj1.price() + myObj2.price() + myObj3.price()
print('Total price is : ', Total)