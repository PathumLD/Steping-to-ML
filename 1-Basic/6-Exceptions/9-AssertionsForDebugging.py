def calculate_discount(price, discount):
    assert 0 <= discount <= 1, "Discount must be between 0 and 1"
    return price * (1 - discount)

try:
    print(calculate_discount(100, 1.5))
except AssertionError as ae:
    print(f"Invalid input: {ae}")