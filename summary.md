# Python Programming Exercises

This repository contains a series of Python programming exercises designed to improve both basic and advanced programming skills. The exercises cover various topics, including string manipulation, function usage, and handling positive and negative numbers.

## Repository Content

1. **[context_managers.py](#context_managers.py-context)**
    - **Description:** This script demonstrates the use of context managers in Python. It includes a class `DatabaseConnection` that simulates opening and closing a database connection using the `__enter__` and `__exit__` methods.
    - **Main Functions:**
        - `__enter__()`: Simulates opening a database connection.
        - `__exit__()`: Simulates closing the database connection.

2. **[add_one.py](#add_one.py-context)**
    - **Description:** This script contains a function `add_one` that adds one to a given number. It handles various edge cases, including non-numeric inputs, NaN, and infinity.
    - **Main Functions:**
        - `add_one(number)`: Adds one to the input number and handles edge cases.

3. **[decorators.py](#decorators.py-context)**
    - **Description:** This script demonstrates the use of decorators in Python. It includes a decorator `call_counter` that counts how many times a decorated function is called.
    - **Main Functions:**
        - `call_counter(func)`: A decorator that adds a call count attribute to the decorated function.

4. **[if_ispositive.py](#if_ispositive.py-context)**
    - **Description:** This script contains functions to check if a number is positive or negative. It handles various edge cases, including non-numeric inputs, NaN, and infinity.
    - **Main Functions:**
        - `is_positive(number)`: Checks if the input number is positive.
        - `is_negative(number)`: Checks if the input number is negative.

5. **[is_odd.py](#is_odd.py-context)**
    - **Description:** This script contains a function `is_odd` that checks if a given number is odd. It handles various edge cases, including non-numeric inputs, NaN, and infinity.
    - **Main Functions:**
        - `is_odd(number)`: Checks if the input number is odd.

6. **[logging_example.py](#logging_example.py-context)**
    - **Description:** This script demonstrates the use of the logging module in Python. It includes examples of different logging levels and how to configure logging.
    - **Main Functions:**
        - `setup_logging()`: Configures the logging settings.
        - `log_messages()`: Logs messages at different levels.

7. **[namespace.py](#namespace.py-context)**
    - **Description:** This script demonstrates the use of namespaces in Python. It includes examples of global, local, and built-in namespaces, and shows how to access and modify them.
    - **Main Functions:**
        - `my_function()`: Demonstrates accessing and modifying a global variable.
        - `my_function_with_locals()`: Displays the local namespace inside a function.
        - `modify_global()`: Modifies a global variable.
        - `my_function_with_locals_modification()`: Attempts to modify the local namespace using locals().

8. **[plus_two.py](#plus_two.py-context)**
    - **Description:** This script contains a function `plus_two` that adds two to a given number. It handles various edge cases, including non-numeric inputs, NaN, and infinity.
    - **Main Functions:**
        - `plus_two(number)`: Adds two to the input number and handles edge cases.

9. **[Positive_and_Negative_numbers.py](#Positive_and_Negative_numbers.py-context)**
    - **Description:** This script generates and handles positive and negative numbers. It uses the `random` library to generate random numbers and organizes them into lists of positive and negative numbers. It includes functions to iterate over these numbers and print them.
    - **Main Functions:**
        - `loop_numbers()`: Populates the `list_positive_numbers` and `list_negative_numbers` lists with positive and negative numbers, respectively.
        - `printumbers()`: Prints the even positive and negative numbers from the lists.

10. **[process_argument.py](#process_argument.py-context)**
    - **Description:** This script contains a function `process_argument` that processes positional and keyword arguments, converting them to strings and returning them as a tuple of a list and a dictionary.
    - **Main Functions:**
        - `process_argument(*args, **kwargs)`: Converts positional and keyword arguments to strings and returns them.

11. **[Python_Exercises.py](#Python_Exercises.py-context)**
    - **Description:** This script contains a series of Python exercises designed to improve programming skills. It includes various functions that demonstrate different programming concepts.
    - **Main Functions:**
        - Various functions demonstrating different programming concepts.

12. **[say_hello.py](#say_hello.py-context)**
    - **Description:** This script contains a simple function `say_hello` that prints a greeting message.
    - **Main Functions:**
        - `say_hello(name)`: Prints a greeting message with the given name.

13. **[sqlite_example.py](#sqlite_example.py-context)**
    - **Description:** This script demonstrates the use of SQLite in Python. It includes examples of creating a database, inserting data, and querying data.
    - **Main Functions:**
        - `create_database()`: Creates a new SQLite database.
        - `insert_data()`: Inserts data into the database.
        - `query_data()`: Queries data from the database.

14. **[functional_programming.py](#functional_programming.py-context)**
    - **Description:** This script demonstrates various functional programming concepts in Python, including the use of named tuples, lambda functions, higher-order functions, and functions as first-class objects.
    - **Main Functions:**
        - `get_position(worker)`: Lambda function to get the position of a worker.
        - `greet(func)`: Function that takes another function as an argument and prints a greeting.
        - `parent()`: Function that returns another function.

15. **[concurrent_programming.py](#concurrent_programming.py-context)**
    - **Description:** This script demonstrates the use of threading in Python. It includes examples of creating and running threads to perform concurrent tasks.
    - **Main Functions:**
        - `task1()`: Simulates a task by printing steps and sleeping.
        - `task2()`: Simulates another task by printing steps and sleeping.
        - `run_tasks()`: Creates and starts threads for `task1` and `task2`, and waits for them to finish.

## Requirements

- Python 3.x
- `random` library (included in Python's standard library)

## Contributions

Contributions are welcome! Feel free to open issues or pull requests to improve these exercises or add new ones.

## License

NO License
