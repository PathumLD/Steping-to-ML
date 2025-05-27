name = "Alice"
age = 30

# Old style formatting
message1 = "My name is %s and I am %d years old." % (name, age)

# String format() method
message2 = "My name is {} and I am {} years old.".format(name, age)

# f-strings (Python 3.6+)
message3 = f"My name is {name} and I am {age} years old."

print(message1)  # Outputs: My name is Alice and I am 30 years old.
print(message2)  # Outputs: My name is Alice and I am 30 years old.
print(message3)  # Outputs: My name is Alice and I am 30 years old.