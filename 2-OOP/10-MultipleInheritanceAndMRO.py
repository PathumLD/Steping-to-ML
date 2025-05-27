"""
Python supports multiple inheritance, where a class can inherit from multiple parent classes.
The Method Resolution Order (MRO) defines the order in which base classes are searched when executing a method.
"""



class A:
    def do(self):
        print("A")

class B:
    def do(self):
        print("B")

class C(A, B):
    pass

c = C()
c.do()  # Output: A (MRO: C → A → B)



class Device:
    def __init__(self, device_type):
        self.type = device_type
        self.power = False
    
    def power_on(self):
        self.power = True
        return f"{self.type} powered on"
    
    def power_off(self):
        self.power = False
        return f"{self.type} powered off"

class Wireless:
    def __init__(self):
        self.connected = False
    
    def connect(self):
        self.connected = True
        return "Wireless connection established"
    
    def disconnect(self):
        self.connected = False
        return "Wireless connection terminated"

# Multiple inheritance
class SmartPhone(Device, Wireless):
    def __init__(self, brand, model):
        Device.__init__(self, "Smartphone")
        Wireless.__init__(self)
        self.brand = brand
        self.model = model
    
    def info(self):
        power_status = "On" if self.power else "Off"
        connection = "Connected" if self.connected else "Disconnected"
        return f"{self.brand} {self.model} - Power: {power_status}, Wireless: {connection}"

# Create a smartphone
my_phone = SmartPhone("Samsung", "Galaxy S21")
print(my_phone.power_on())     # Smartphone powered on
print(my_phone.connect())      # Wireless connection established
print(my_phone.info())         # Samsung Galaxy S21 - Power: On, Wireless: Connected

# Check Method Resolution Order
print(SmartPhone.__mro__)      # Shows the order of method resolution