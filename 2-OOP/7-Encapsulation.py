"""
Encapsulation is the bundling of data (attributes) and methods that operate on that data within a single unit (class), and restricting direct access to some of the object's components.
In Python, encapsulation is achieved through naming conventions rather than strict access modifiers.

Private Attributes and Methods

Theory:

    Single underscore _ prefix: Conventional indication that an attribute/method is intended for internal use
    Double underscore __ prefix: Name mangling - Python renames the attribute to avoid name conflicts in subclasses

Encapsulation means hiding internal object details and only exposing necessary parts through public methods.
Python doesn't have true private variables, but uses conventions:

    _var → protected (by convention)

    __var → private (name mangled)

"""


# Private Variables
class myVar:
    x=10   #Public Variable
    __y=20 #Private Variable

    #Method to access private variable
    def disp(self):
        return self.__y

myObj1 = myVar()
print(myObj1.x)
print(myObj1.disp())


# Private Methods
class myMeth:
    def meth1(self):   #Public Method
        print("Meth1")
        self.__meth2() #calling to private method throu the public method since public method has access

    def __meth2(self): #Private Method
        print("Meth2")

myObj2 = myMeth()
myObj2.meth1()



class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # private attribute

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age



class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner           # public attribute
        self._balance = balance      # protected attribute (convention)
        self.__transaction_log = []  # private attribute (name mangling)
    
    def deposit(self, amount):
        self._balance += amount
        self.__log_transaction("deposit", amount)
        return self._balance
    
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            self.__log_transaction("withdrawal", amount)
            return self._balance
        return "Insufficient funds"
    
    def __log_transaction(self, transaction_type, amount):
        # Private method
        self.__transaction_log.append(f"{transaction_type}: ${amount}")
    
    def get_balance(self):
        return self._balance
    
    def get_transaction_history(self):
        return self.__transaction_log

account = BankAccount("Alice", 1000)
print(account.deposit(500))        # 1500
print(account.withdraw(200))       # 1300
print(account.get_balance())       # 1300

# Direct access attempt
print(account.owner)               # Alice (public attribute)
print(account._balance)            # 1300 (protected - accessible but not recommended)
# print(account.__transaction_log)  # AttributeError (private attribute)