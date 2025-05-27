# Dictionary comprehension
squares = {x: x*x for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Merging dictionaries (Python 3.9+)
defaults = {'color': 'red', 'size': 'medium'}
custom = {'size': 'large', 'price': 10.5}
combined = defaults | custom

# Default dictionaries
from collections import defaultdict
word_counts = defaultdict(int)
for word in ['apple', 'banana', 'apple']:
    word_counts[word] += 1

# Dictionary unpacking
def connect(**config):
    print(f"Connecting with {config}")

db_config = {'host': 'localhost', 'port': 5432}
connect(**db_config)