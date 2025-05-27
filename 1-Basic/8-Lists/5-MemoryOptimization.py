import sys

# Size comparison
empty_list = []
small_list = [1]
large_list = list(range(1000))

print(sys.getsizeof(empty_list))  # ~56 bytes (overhead)
print(sys.getsizeof(small_list))  # ~64 bytes 
print(sys.getsizeof(large_list))  # ~8056 bytes

# Pre-allocation optimization
# Instead of appending in loop:
result = []
for x in range(1000):
    result.append(x*2)

# Pre-allocate:
result = [None] * 1000
for i in range(1000):
    result[i] = i * 2