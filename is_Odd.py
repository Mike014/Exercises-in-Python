def is_odd(number):
    try:
        number = float(number)
    except ValueError:
        raise ValueError("The input must be a number")

    if number.is_integer():
        number = int(number)

    if number % 2 == 0:
        return False
    else:
        return True

# Function tests
assert is_odd(5) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_odd(4) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_odd(-3) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_odd("-4") == False, "Ensure that the function is defined, named properly, and returns the correct value"

try:
    is_odd(float('nan'))
except ValueError as error:
    assert str(error) == "The input must be a number", "Ensure that the function is defined, named properly, and returns the correct value"

try:
    is_odd(float('inf'))
except ValueError as error:
    assert str(error) == "The input must be a number", "Ensure that the function is defined, named properly, and returns the correct value"

print("The function is_odd works correctly")



