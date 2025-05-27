def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished executing {func.__name__}")
        return result
    return wrapper

@log_execution
def complex_calculation(x, y):
    return x * y + x / y

print(complex_calculation(10, 5))