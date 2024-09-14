# Create a decorator called call_counter that counts how many times a decorated function is called.
# The decorator should add a call_count attribute to the decorated function, which keeps track of the number of calls.

def call_counter(func):
    def wrapper(*args, **kwargs):
        # Increment the call count
        wrapper.call_count += 1
        
        # Call the original function with its arguments
        result = func(*args, **kwargs)
        
        # Return the result of the original function
        return result
    
    # Initialize the call count attribute
    wrapper.call_count = 0
    
    # Return the wrapper function
    return wrapper

@call_counter
def say_hello(name):
    print(f'Hello, {name}!')

# Test the decorated function
say_hello('John')
say_hello('Linda')

# Print the call count
print(say_hello.call_count)  # Output: 2





