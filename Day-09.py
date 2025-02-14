# Functions and Exception Handling in Python

## Function Basics

### Defining a Function
"""A function in Python is defined using the `def` keyword. Functions help in modularizing the code, improving readability, and avoiding repetition."""

def greet(name):
    """Function to greet a user"""
    return f"Hello, {name}! Welcome to Python programming."

# Calling the function
print(greet("Alice"))

### Function with Parameters and Default Values
"""Functions can take parameters, and default values can be assigned to them."""

def add_numbers(a, b=10):
    """Returns the sum of two numbers with a default value for b"""
    return a + b

print(add_numbers(5))  # Uses default b=10
print(add_numbers(5, 20))  # Overriding default value

### Variable-Length Arguments
"""We can pass a variable number of arguments using `*args`."""

def sum_all(*numbers):
    """Returns the sum of all provided numbers"""
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5))

### Keyword Arguments
"""Keyword arguments allow passing parameters in any order by explicitly specifying the argument names."""

def display_info(name, age):
    """Displays user info"""
    print(f"Name: {name}, Age: {age}")

display_info(age=25, name="Bob")  # Using keyword arguments

### Lambda Functions
"""A lambda function is an anonymous function that is defined using the `lambda` keyword.

- **Syntax:** `lambda arguments: expression`
- **Usage:** Useful for short functions that are not reused multiple times.
"""
square = lambda x: x * x
print(f"Square of 4: {square(4)}")

add = lambda x, y: x + y
print(f"Sum of 3 and 7: {add(3, 7)}")

## Exception Handling

### Why Exception Handling?
"""Errors can occur during execution (runtime errors). To prevent crashes, Python provides exception handling using `try`, `except`, `finally`, and `raise`."""

### Handling Exceptions with try-except
"""The `try` block contains the code that might cause an error. The `except` block handles the error gracefully."""

def divide(a, b):
    """Performs division with exception handling"""
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Invalid input type. Please provide numbers.")
        return None
    else:
        print("Division successful!")
        return result
    finally:
        print("Execution of divide function completed.")

print(divide(10, 2))
print(divide(10, 0))
print(divide(10, "a"))

### Raising Exceptions
"""Sometimes, we need to manually raise an exception using the `raise` keyword."""

def check_age(age):
    """Checks if age is valid"""
    if age < 18:
        raise ValueError("Age must be 18 or older!")
    return "Access Granted"

try:
    print(check_age(15))
except ValueError as e:
    print(f"Exception: {e}")