def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))  # 6
print(sum_all(4, 5))     # 9

def create_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

create_profile(name="Alice", age=30, occupation="Engineer")