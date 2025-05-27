try:
    result = 100 / int(input("Divisor: "))
except ValueError:
    print("Must enter a number")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Result is {result}")
finally:
    print("This always runs")