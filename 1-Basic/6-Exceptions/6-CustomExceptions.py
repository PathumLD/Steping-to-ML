class InvalidEmailError(Exception):
    """Raised when email format is invalid"""
    def __init__(self, email):
        self.email = email
        super().__init__(f"Invalid email format: {email}")

def send_email(address):
    if "@" not in address:
        raise InvalidEmailError(address)
    # Send email logic...

try:
    send_email("user.example.com")
except InvalidEmailError as iee:
    print(iee)