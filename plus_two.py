# -*- coding: utf-8 -*-

def plus_two(number):
    try:
        number = float(number)
    except ValueError:
        raise ValueError("The input must be a number")

    result = number + 2

    if result.is_integer():
        return int(result)

    return result


assert plus_two(3) == 5, "Double check the inputs and data types"
assert plus_two(0) == 2, "Double check the inputs and data types"
assert plus_two(-2) == 0, "Double check the inputs and data types"
assert plus_two(0.5) == 2.5, "Double check the inputs and data types"
assert plus_two(-1.5) == 0.5, "Double check the inputs and data types"

try:
    plus_two("a")
except ValueError as error:
    assert str(error) == "The input must be a number", "Double check the inputs and data types"

print("The example function ran correctly")




