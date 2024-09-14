import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('app.log')
    ]
)

# Create a logger
logger = logging.getLogger('my_logger')

# Log some messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message') 
logger.error('This is an error message')
logger.critical('This is a critical message')


def divide(a, b):
    try:
        result = a / b
        logger.info("Division successful")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero!")

# Test the divide function
assert divide(10, 2) == 5
assert divide(5, 0) == None
assert divide(8, 4) == 2
print("All tests passed successfully")

# The logging module in Python provides a flexible and powerful framework for generating log messages from your code.
