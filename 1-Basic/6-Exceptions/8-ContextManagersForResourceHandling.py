class DatabaseConnection:
    def __enter__(self):
        print("Opening connection")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing connection")
        if exc_type:
            print(f"Error occurred: {exc_val}")
        return True  # Suppress exception

with DatabaseConnection() as db:
    print("Using database")
    raise ValueError("DB operation failed")