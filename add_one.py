# -*- coding: utf-8 -*-
import math

def add_one(number):
    try:
        number = float(number)
    except ValueError:
        raise ValueError("The input must be a number")

    if math.isnan(number):
        raise ValueError("The input must be a number")

    if math.isinf(number):
        raise ValueError("The input must be a number")
 
    result = number + 1

    if result.is_integer():
        return int(result)

    return result

# Function tests
assert add_one(2) == 3, "Double check the inputs and data types"
assert add_one(0) == 1, "Double check the inputs and data types"
assert add_one("5") == 6, "Double check the inputs and data types"
assert add_one(6.55) == 7.55, "Double check the inputs and data types"

try:
    add_one(float('nan'))
except ValueError as error:
    assert str(error) == "The input must be a number", "Double check the inputs and data types"

try:
    add_one(float('inf'))
except ValueError as error:   
    assert str(error) == "The input must be a number", "Double check the inputs and data types"

print("The example function ran correctly")



