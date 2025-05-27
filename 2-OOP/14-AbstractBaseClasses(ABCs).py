"""
Abstract Base Classes (ABCs) are classes that cannot be instantiated and are designed to serve as a base class for other classes.
They ensure that derived classes implement certain methods.
"""


from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        print("Driving a car")



from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount
    
    @abstractmethod
    def process_payment(self):
        pass
    
    @abstractmethod
    def payment_details(self):
        pass
    
    # Non-abstract method
    def payment_confirmation(self):
        return f"Payment of ${self.amount} confirmed"

class CreditCardPayment(Payment):
    def __init__(self, amount, card_number, expiry):
        super().__init__(amount)
        self.card_number = card_number
        self.expiry = expiry
    
    def process_payment(self):
        # Implementation specific to credit card
        return f"Processing ${self.amount} payment with card {self.card_number[-4:]}"
    
    def payment_details(self):
        return f"Credit card payment: Card ending with {self.card_number[-4:]}, Expiry: {self.expiry}"

class PayPalPayment(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email
    
    def process_payment(self):
        # Implementation specific to PayPal
        return f"Processing ${self.amount} payment via PayPal account {self.email}"
    
    def payment_details(self):
        return f"PayPal payment: Account {self.email}"

# Create payment methods
# payment = Payment(100)  # TypeError: Can't instantiate abstract class
cc_payment = CreditCardPayment(100, "1234567890123456", "12/25")
paypal_payment = PayPalPayment(75.50, "example@email.com")

# Process payments
print(cc_payment.process_payment())
print(cc_payment.payment_details())
print(cc_payment.payment_confirmation())

print(paypal_payment.process_payment())
print(paypal_payment.payment_details())
print(paypal_payment.payment_confirmation())