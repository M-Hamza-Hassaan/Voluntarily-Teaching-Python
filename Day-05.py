# Introduction to Conditions in Python (if, elif, else & Short-hand Conditions)

# 1. Basic if statement
x = 3
if x > 5:
    print("x is greater than 5")

# 2. if-else statement
y = 3
if y % 2 == 1:
    print("y is non-even")
else:
    print("y is even")

# 3. if-elif-else statement
score = 70
if score >= 90:
    print("Grade: A")
elif score >= 80:

    # a = 5
    # b = 10
    # print(a+b)
    print("Grade: B")

elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# 4. Nested if statements
num = 15

if num > 10:
    print("Number is greater than 10")
    if num % 5 == 0:
        print("Number is also a multiple of 5")
        if num < 20:
            print("Num is 15")

# Practice
# Write a program that takes an integer input representing a person's age and classifies them into the following groups:

# Child (0-12 years)
# Teenager (13-19 years)
# Adult (20-59 years)
# Senior (60 years and above)
# Use an if-elif-else statement.



                     