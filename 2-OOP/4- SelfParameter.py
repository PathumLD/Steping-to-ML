"""
In Python, self is a reference to the current instance of the class.
It's used to access variables and methods belonging to the class. It's automatically passed as the first parameter to all methods in a class.
"""


class Person:
    def introduce(self):
        # Using self to refer to the current instance
        return "Hello, I am a person!"
    
    def think(self, thought):
        # self is used to reference the method's instance
        return f"I am thinking about {thought}"

someone = Person()
print(someone.introduce())
print(someone.think("Python OOP"))