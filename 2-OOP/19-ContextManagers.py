"""
Context managers define the runtime context that is entered using the with statement. They handle setup and teardown operations.
"""


class MyContext:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")

with MyContext():
    print("Inside context")




class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"Opening {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing {self.filename}")
        if self.file:
            self.file.close()
        # Return True to suppress exception, False to propagate it
        return False

# Using our custom context manager
try:
    with FileManager("example.txt", "w") as f:
        f.write("Hello, World!")
        print("File written successfully")
        # Uncomment to test exception handling
        # raise ValueError("Test exception")
except Exception as e:
    print(f"Error: {e}")