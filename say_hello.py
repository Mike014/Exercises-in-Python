# -*- coding: utf-8 -*-

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




