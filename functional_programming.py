from collections import namedtuple
from functools import reduce

# Define an immutable tuple
immutable_data = (1, 2, 3, 4, 5)

# Define a named tuple
Worker = namedtuple('Worker', ['name', 'age', 'position'])

# Create a list of workers
people = [
    Worker(name='John', age=30, position='Developer'),
    Worker(name='Jane', age=28, position='Designer'),
    Worker(name='Dave', age=35, position='Manager')
]

# Lambda function to get the position of a worker
get_position = lambda worker: worker.position
print(list(map(get_position, people)))
# Output: ['Developer', 'Designer', 'Manager']

# Apply higher-order function to get ages of workers
ages = list(map(lambda worker: worker.age, people))
print(ages)
# Output: [30, 28, 35]

# Filter the list of workers by age
filtered_people = list(filter(lambda worker: worker.age <= 30, people))
print(filtered_people)
# Output: [Worker(name='John', age=30, position='Developer'), Worker(name='Jane', age=28, position='Designer')]

# Reduce the list of ages to get the total age
total_age = reduce(lambda x, y: x + y, ages)
print(total_age)
# Output: 93

# Functions as first-class objects
# Assign a function to a variable
uppercase = str.upper
big_pie = uppercase('pie')
print(big_pie)
# Output: PIE

# Define a function that takes another function as an argument
def greet(func):
    greeting = func('Hello')
    print(greeting)

# Call the function and pass another function as an argument
greet(str.upper)
# Output: HELLO

# Define a function that returns another function
def parent():
    def first_child():
        return "Printing from the first child function"
    return first_child

# Assign the returned function to a variable
first_child = parent()
print(first_child())
# Output: Printing from the first child function
