# -*- coding: utf-8 -*-

# Write a function say_hello that adds the string "Hello, " at the beginning and "!" at the end of any given input.
# The function should also correctly handle cases where the input is empty or contains only whitespace, returning "Hello, World!" in such cases. Additionally,
# the function should be able to handle inputs that are not strings, converting them to strings before adding the greeting.

def say_hello(name):
    if not isinstance(name, str):
        name = str(name)
    name = name.strip() # Removes whitespace at the beginning and end of the string
    if not name:
        name = "World"
    return f"Hello, {name}!"

# Function tests
assert say_hello("Jane") == "Hello, Jane!", "Double check the inputs and data types"
assert say_hello("Pat") == "Hello, Pat!", "Double check the inputs and data types"
assert say_hello("Astrud") == "Hello, Astrud!", "Double check the inputs and data types"
assert say_hello("") == "Hello, World!", "Double check the inputs and data types"
assert say_hello("   ") == "Hello, World!", "Double check the inputs and data types"
assert say_hello(123) == "Hello, 123!", "Double check the inputs and data types"
assert say_hello(None) == "Hello, None!", "Double check the inputs and data types"
print("The example function ran correctly")



