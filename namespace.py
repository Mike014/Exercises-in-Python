# Global variable
x = 10

def my_function():
    global x  # Declare x as a global variable
    # Local variable
    y = 20

    print("Value of x (global):", x)  # Access global namespace
    print("Value of y (local):", y)   # Access local namespace
    
    # Modify a global variable
    x = 20  # Modify global x

# Access built-in functions
print("Length of 'Python':", len("Python"))  # Built-in namespace
print("Type of 'Python':", type("Python"))   # Built-in namespace
print("Max of 'Python':", max("Python"))     # Built-in namespace
print("Min of 'Python':", min("Python"))     # Built-in namespace

my_function()

# Access the modified global variable
print("Modified value of x (global):", x)

# Access the global namespace
def my_function_with_locals():
    y = 5  # Local variable
    print("Local namespace inside the function:", locals())  # Display local namespace

my_function_with_locals()
print("Global namespace:", globals())

# Built-in module: Contains the built-in namespace with all built-in functions and exceptions
print("Built-in namespace:", dir(__builtins__))

# Modify Global Variables:
def modify_global():
    global x
    x = 30  # Modify global variable x

modify_global()
print("New value of x (global):", x)

# Modify Local Namespace:
def my_function_with_locals_modification():
    y = 5
    print("Local namespace:", locals())
    locals()['y'] = 10  # This does not actually modify y
    print("Value of y after locals():", y)  # y remains 5

my_function_with_locals_modification()


# What are Namespaces?
# In Python, namespaces are containers that map names to objects. Whenever you create a variable or define a function, Python associates that name with an object in a specific namespace. There are different levels of namespaces, including local, global, and built-in namespaces.
# Types of Namespaces:
# 1.	Local Namespace: Associated with a function or method, it contains names defined within the function.
# 2.	Global Namespace: Associated with the module, it contains names defined at the top level of the module.
# 3.	Built-in Namespace: Contains predefined names that Python provides automatically, such as the functions len(), print(), etc.