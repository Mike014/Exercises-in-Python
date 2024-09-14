class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        # Simulate opening a database connection
        self.connection = f"Connection to {self.db_name}"
        print(f"Opening {self.connection}")
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Simulate closing the database connection
        if self.connection:
            print(f"Closing {self.connection}")
            self.connection = None

# Test the context manager
with DatabaseConnection('example.db') as conn:
    print(f"Using {conn} to perform database operations")

# Context managers in Python are a feature that allows for efficient and safe resource management,
# ensuring that setup and teardown operations are performed correctly.
# They are commonly used to manage resources such as files, database connections,
# and other resources that need to be opened and closed in a controlled manner.
