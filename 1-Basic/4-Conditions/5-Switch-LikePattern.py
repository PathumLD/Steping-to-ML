def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Dictionary mapping operation names to functions
operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}

# Using the dictionary as a switch
operation = "multiply"
x, y = 10, 5

if operation in operations:
    result = operations[operation](x, y)
    print(f"Result of {operation}: {result}")  # Outputs: Result of multiply: 50
else:
    print("Invalid operation")