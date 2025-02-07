# Python Operators Explained with Examples

# Arithmetic Operators
# These operators perform mathematical operations like addition, subtraction, multiplication, etc.
a = 10
b = 3

print('Arithmetic Operators:')

# print(f'Addition: {a} + {b} = {a + b}')       # Addition
# print(f'Subtraction: {a} - {b} = {a - b}')    # Subtraction
# print(f'Multiplication: {a} * {b} = {a * b}')  # Multiplication
# print(f'Division: {a} / {b} = {a / b}')      # Division

# print(f'Floor Division: {a} // {b} = {a // b}') # Floor Division

# ceil=>3.1=4, floor=> 3.9=3
# print(f'Modulus: {a} % {b} = {a % b}')      # Modulus (Remainder)
# print(f'Exponentiation: {a} ** {b} = {a ** b}') # Exponentiation

# # 2. Assignment Operators
# # # Used to assign values to variables
# x = 5  # Assigning value
# x += 3  # Equivalent to x = x + 3
# x -= 2  # Equivalent to x = x - 2
# x *= 4  # Equivalent to x = x * 4

# x /= 2  # Equivalent to x = x / 2
# x %= 3  # Equivalent to x = x % 3
# print('\nAssignment Operators:')
# print(f'Final value of x after assignments: {x}')

# # 3. Comparison Operators
# # Used to compare values
print('\nComparison Operators:')
print(f'{a} == {b}:', a == b)  # Equal to
print(f'{a} != {b}:', a != b)  # Not equal to
print(f'{a} > {b}:', a > b)    # Greater than
print(f'{a} < {b}:', a < b)    # Less than
print(f'{a} >= {b}:', a >= b)  # Greater than or equal to
print(f'{a} <= {b}:', a <= b)  # Less than or equal to

# # 4. Logical Operators
# # Used to combine conditional statements
# print('\nLogical Operators:')
# print(f'({a} > {b}) and ({a} < 20):', (a > b) and (a < 20))  # AND operator
# print(f'({a} > 20) or ({b} < 5):', (a > 20) or (b < 5))      # OR operator
# print(f'not ({a} > {b}):', not (a > b))                      # NOT operator


# ---Assignment---
# Write a Python program that allows the user to input two numbers and then:
#    - Perform all arithmetic operations on them
#    - Display the results