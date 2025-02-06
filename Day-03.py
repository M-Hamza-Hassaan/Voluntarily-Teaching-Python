# 1. Types of Strings
# -------------------------------
# Single and double quotes
str1 = 'Hello'

str2 = "World"

print(str1 + str2)

# Triple-quoted strings (multi-line)
message = """This is  
a multi-line  
string."""

print(message)

# Raw strings (ignores escape sequences)
# r means read, is a flag
# read krna hy, path of a file
raw_path = r"C:\Users\Python\Documents"

# f-Strings for formatting
name = "Hammad"
age = 19
formatted_string = f"My name is {name} and I am {age} years old."

# Printing examples
print(str1, str2)
print(message)
print(raw_path)
print(formatted_string)

# -------------------------------
# 2. Keywords in Python
# -------------------------------

import keyword

# Display all Python keywords
print("Python Keywords:", keyword.kwlist)

# Example usage of keywords
def check_number(num):
    """Function to check if a number is positive, negative, or zero"""
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(check_number(10))

# -------------------------------
# 3. Type Casting
# -------------------------------

# Implicit Type Casting
num1 = 10   # int
num2 = 3.59235749  # float
result = num1 + num2  # int + float = float (Python automatically converts)
result_in_int = int(num1 + num2)  # int + float = float (Python automatically converts)
print(result, type(result))  # Output: 13.5 <class 'float'>
print(result_in_int, type(result_in_int))  # Output: 13.5 <class 'float'>

# Explicit Type Casting
num_str = "50" #string
num_int = int(num_str)  # Convert string to integer
num_float = float(num_int)  # Convert integer to float
num_str_back = str(num_float)  # Convert float back to string

print(num_int, type(num_int))
print(num_float, type(num_float))
print(num_str_back, type(num_str_back))



# practice:

# Write code to get this output

# Output: "ALI52"