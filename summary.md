# Python Programming Exercises
# Python Programming Exercises

This repository contains a series of Python programming exercises designed to improve both basic and advanced programming skills. The exercises cover various topics, including string manipulation, function usage, and handling positive and negative numbers.

## Repository Content

1. **context_managers.py**
    - **Description:** This script demonstrates the use of context managers in Python. It includes a class `DatabaseConnection` that simulates opening and closing a database connection using the `__enter__` and `__exit__` methods.
    - **Main Functions:**
        - `__enter__()`: Simulates opening a database connection.
        - `__exit__()`: Simulates closing the database connection.

2. **add_one.py**
    - **Description:** This script contains a function `add_one` that adds one to a given number. It handles various edge cases, including non-numeric inputs, NaN, and infinity.
    - **Main Functions:**
        - `add_one(number)`: Adds one to the input number and handles edge cases.

3. **decorators.py**
    - **Description:** This script demonstrates the use of decorators in Python. It includes a decorator `call_counter` that counts how many times a decorated function is called.
    - **Main Functions:**
        - `call_counter(func)`: A decorator that adds a call count attribute to the decorated function.

4. **if_ispositive.py**
    - **Description:** This script contains functions to check if a number is positive or negative. It handles various edge cases, including non-numeric inputs, NaN, and infinity.
    - **Main Functions:**
        - `is_positive(number)`: Checks if the input number is positive.
        - `is_negative(number)`: Checks if the input number is negative.

5. **is_Odd.py**
    - **Description:** This script contains a function `is_odd` that checks if a given number is odd. It handles various edge cases, including non-numeric inputs, NaN, and infinity.
    - **Main Functions:**
        - `is_odd(number)`: Checks if the input number is odd.

6. **plus_two.py**
    - **Description:** This script contains a function `plus_two` that adds two to a given number. It handles various edge cases, including non-numeric inputs, NaN, and infinity.
    - **Main Functions:**
        - `plus_two(number)`: Adds two to the input number and handles edge cases.

7. **Positive_and_Negative_numbers.py**
    - **Description:** This script generates and handles positive and negative numbers. It uses the `random` library to generate random numbers and organizes them into lists of positive and negative numbers. It includes functions to iterate over these numbers and print them.
    - **Main Functions:**
        - `loop_numbers()`: Populates the `list_positive_numbers` and `list_negative_numbers` lists with positive and negative numbers, respectively.
        - `printumbers()`: Prints the even positive and negative numbers from the lists.

8. **process_argument.py**
    - **Description:** This script contains a function `process_argument` that processes positional and keyword arguments, converting them to strings and returning them as a tuple of a list and a dictionary.
    - **Main Functions:**
        - `process_argument(*args, **kwargs)`: Converts positional and keyword arguments to strings and returns them.

## Requirements

- Python 3.x
- `random` library (included in Python's standard library)

## Contributions

Contributions are welcome! Feel free to open issues or pull requests to improve these exercises or add new ones.

## License

NO License

