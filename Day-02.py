"""

print()
comment

= is variable assignment operator
== identifier

primitive datatype: int, float, string
other data types: bool, set(), null, object

type conversion: from int to float, from string to int, from string to bool

take input data from user.
"""

# print() and comments (#)
# The print() function is used to display output.

# print("Hello, students! Welcome to Python Sessions.")  

# This is a comment

# Understanding identifiers and variable assignment
# student_name = "Hamza" #string # Valid identifier and variable assignment
# age = 22  # Integer assignment
# is_enrolled = True  # Boolean assignment

# print ( student_name ,type(student_name))  # Checking type of variable
# print(age, type(age))
# type_of_is_enrolled = type(is_enrolled)
# print(is_enrolled, type(is_enrolled))

# print("Student Name:", student_name)
# print("Age:", age)
# print("Enrolled:", is_enrolled)
# print("Type of student_name:", type_of_student_name)
# print("Type of age:", type_of_age)
# print("Type of is_enrolled:", type_of_is_enrolled)


#  Primitive data types: int, float, str, bool
# integer_value = 10
# float_value = 10.5
# string_value = "Python"
# boolean_value = True

# print("Integer Value:", integer_value)
# print("Float Value:", float_value)
# print("String Value:", string_value)
# print("Boolean Value:", boolean_value)

# # Type checking with type()
# print("Type of integer_value:", type(integer_value))
# print("Type of float_value:", type(float_value))
# print("Type of string_value:", type(string_value))
# print("Type of boolean_value:", type(boolean_value))

# print(type(user_phone_number))

# # Type conversion using int(), float(), str(), bool()
# num_str = "25"
# num_int = int(num_str)  # Convert string to integer
# num_float = float(num_str)  # Convert string to float
# num_bool = bool(num_str)  # Convert string to boolean (True if not empty)

# print("Converted to Integer:", num_int)
# print("Converted to Float:", num_float)
# print("Converted to Boolean:", num_bool)

# practice:

# # Taking user input using input() and converting data types
user_name = input("Enter your name: ")  # String input
user_age = int(input("Enter your age: "))  # Convert input string to integer
user_height = float(input("Enter your height in meters: "))  # Convert input string to float

print("Hello,", user_name, "You are", user_age, "years old and", user_height, "meters tall.")
