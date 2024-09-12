# Python Programming Exercises

This repository contains a series of Python programming exercises designed to improve both basic and advanced programming skills. The exercises cover various topics, including string manipulation, function usage, and handling positive and negative numbers.

## Repository Content

1. **say_hello.py**
    - **Description:** This script contains a function `say_hello` that adds the string "Hello, " at the beginning and "!" at the end of any given input. The function correctly handles cases where the input is empty or contains only whitespace, returning "Hello, World!" in such cases. Additionally, the function can handle inputs that are not strings, converting them to strings before adding the greeting.
    - **Usage Examples:**

2. **Positive_and_Negative_numbers.py**
    - **Description:** This script generates and handles positive and negative numbers. It uses the `random` library to generate random numbers and organizes them into lists of positive and negative numbers. It includes functions to iterate over these numbers and print them.
    - **Main Functions:**
        - `loop_numbers()`: Populates the `list_positive_numbers` and `list_negative_numbers` lists with positive and negative numbers, respectively.
        - `printumbers()`: Prints the even positive and negative numbers from the lists.

3. **add_one.py**
    - **Description:** This script contains a function `add_one` that takes a number as input and returns that number incremented by one. The function handles non-numeric inputs by raising an appropriate exception and also manages special cases like `NaN` and `infinity`.
    - **Main Functions:**
        - `add_one(number)`: Converts the input to a float, checks for `NaN` and `infinity`, adds one to the number, and returns the result as an integer if applicable.

4. **plus_two.py**
    - **Description:** This script contains a function `plus_two` that takes a number as input and returns that number incremented by two. The function handles non-numeric inputs by raising an appropriate exception.
    - **Main Functions:**
        - `plus_two(number)`: Converts the input to a float, adds two to the number, and returns the result as an integer if applicable.

## Requirements

- Python 3.x
- `random` library (included in Python's standard library)

## Contributions

Contributions are welcome! Feel free to open issues or pull requests to improve these exercises or add new ones.

## License

NO License.
