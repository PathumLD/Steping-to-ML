"""
Class variables are shared among all instances of a class
Instance variables are unique to each instance
"""



class Dog:
    species = "Canine"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable



class Employee:
    # Class variable
    company = "Tech Corp"
    
    def __init__(self, name, salary):
        # Instance variables
        self.name = name
        self.salary = salary
    
    def get_details(self):
        return f"{self.name} works at {Employee.company} and earns ${self.salary}"

# Two different employees
emp1 = Employee("John", 50000)
emp2 = Employee("Sarah", 60000)

print(emp1.get_details())
print(emp2.get_details())

# Change the class variable
Employee.company = "New Corp"

# Both instances reflect the change
print(emp1.company)  # "New Corp"
print(emp2.company)  # "New Corp"