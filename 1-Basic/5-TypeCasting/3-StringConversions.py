# Number to string
age = 25
age_str = str(age)
print("I am " + age_str + " years old")  # Concatenation

# List to string
lst = [1, 2, 3]
lst_str = str(lst)  # "[1, 2, 3]"
print(lst_str[0])  # "["

# Proper list to string
proper_str = ", ".join(map(str, lst))
print(proper_str)  # "1, 2, 3"