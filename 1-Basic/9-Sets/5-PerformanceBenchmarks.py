import timeit

# Membership test comparison
list_time = timeit.timeit('"python" in data', 
                  setup='data=list("set theory in python")',
                  number=1000000)

set_time = timeit.timeit('"python" in data', 
                 setup='data=set("set theory in python")',
                 number=1000000)

print(f"List: {list_time:.3f}, Set: {set_time:.3f}")
# Typical output: List: 0.120, Set: 0.040