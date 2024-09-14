def process_argument(*args, **kwargs):
    # *args collects all positional arguments into a tuple
    string_args = [str(arg) for arg in args]
    
    # **kwargs collects all keyword arguments into a dictionary
    string_kwargs = {k: str(v) for k, v in kwargs.items()} 

    # Print the converted arguments for debugging purposes
    print(string_args, string_kwargs)

    # Return the converted arguments as a tuple of a list and a dictionary
    return string_args, string_kwargs

# Test cases to verify the function works as expected
assert process_argument(1, 2, 3, a=4, b=5) == (['1', '2', '3'], {'a': '4', 'b': '5'})
assert process_argument('a', 'b', 'c', d='e', f='g') == (['a', 'b', 'c'], {'d': 'e', 'f': 'g'})
assert process_argument() == ([], {})
assert process_argument(1, 2, 3) == (['1', '2', '3'], {})
assert process_argument(a=4, b=5) == ([], {'a': '4', 'b': '5'})
assert process_argument('a', 'b', 'c') == (['a', 'b', 'c'], {})
assert process_argument(a=4) == ([], {'a': '4'})
assert process_argument('a') == (['a'], {})
assert process_argument(1) == (['1'], {})

# Print a message indicating all tests passed
print('All tests passed!')
