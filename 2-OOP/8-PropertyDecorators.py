"""
Python property decorators provide a way to create getters, setters, and deleters for class attributes, enabling you to control attribute access.
"""



class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value



class Temperature:
    def __init__(self):
        self._celsius = 0
    
    @property
    def celsius(self):
        """Getter method for celsius"""
        print("Getting temperature in Celsius")
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter method for celsius"""
        if value < -273.15:  # Absolute zero check
            raise ValueError("Temperature below absolute zero is not possible")
        print(f"Setting temperature to {value}°C")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Getter method for fahrenheit"""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Setter method for fahrenheit"""
        self.celsius = (value - 32) * 5/9

# Using properties
temp = Temperature()
temp.celsius = 25  # Using the setter
print(temp.celsius)  # Using the getter, returns 25
print(temp.fahrenheit)  # Using the fahrenheit getter, returns 77
temp.fahrenheit = 86  # Using the fahrenheit setter
print(temp.celsius)  # Returns 30