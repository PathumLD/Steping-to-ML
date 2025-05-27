# String to list
s = "hello"
char_list = list(s)
print(char_list)  # ['h', 'e', 'l', 'l', 'o']

# Tuple to list
tup = (1, 2, 3)
lst = list(tup)
print(lst)  # [1, 2, 3]

# Dictionary conversions
d = {'a': 1, 'b': 2}
key_list = list(d)  # ['a', 'b']
items_list = list(d.items())  # [('a', 1), ('b', 2)]