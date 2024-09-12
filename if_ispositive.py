import math

def is_positive(number): 
    try:
        number = float(number)
    except ValueError:
        raise ValueError("The input must be a number")

    if math.isnan(number):
        raise ValueError("The input must be a number")

    if math.isinf(number):
        raise ValueError("The input must be a number")

    if number > 0:
        return True
    else:
        return False

# Function tests
positive_odd_number = 5
positive_even_number = 4
negative_odd_number = -3
negative_even_number = -4

assert is_positive(positive_odd_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_positive(positive_even_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_positive(negative_odd_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_positive(negative_even_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_positive(0) == False, "Zero is not a positive number."
assert is_positive("10") == True, "Ensure that the function is defined, named properly, and returns the correct value"

try:
    is_positive(float('nan'))
except ValueError as error:
    assert str(error) == "The input must be a number", "Ensure that the function is defined, named properly, and returns the correct value"

try:
    is_positive(float('inf'))
except ValueError as error:
    assert str(error) == "The input must be a number", "Ensure that the function is defined, named properly, and returns the correct value"

print("The function is_positive works correctly")


def is_negative(number):
    try:
        number = float(number)
    except ValueError:
        raise ValueError("The input must be a number")

    if math.isnan(number):
        raise ValueError("The input cannot be NaN (Not a Number)")

    if math.isinf(number):
        raise ValueError("The input cannot be infinity")

    if number < 0:
        return True
    else:
        return False


# Function tests
positive_odd_number = 5
positive_even_number = 4
negative_odd_number = -3
negative_even_number = -4

assert is_negative(positive_odd_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_negative(positive_even_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_negative(negative_odd_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_negative(negative_even_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_negative(0) == False, "Zero is not a negative number."

try:
    is_negative(float('nan'))
except ValueError as error:
    assert str(error) == "The input cannot be NaN (Not a Number)", "Ensure that the function handles NaN correctly"

try:
    is_negative(float('inf'))
except ValueError as error:
    assert str(error) == "The input cannot be infinity", "Ensure that the function handles infinity correctly"

print("Exercise 13 is correct.")

                




