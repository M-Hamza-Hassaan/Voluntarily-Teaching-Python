# Python For Loop - Detailed Notebook

# 1. Introduction to For Loop
print("A 'for' loop is used to iterate over a sequence (such as a list, tuple, or string)")

# 2. Basic Syntax
for i in range(5): #5 is where the loop is going to stop
    print(i)  # Output: 0 1 2 3 4

# 3. Iterating Over a List
fruits = ["apple", "banana", "cherry"] #list
for fruit in fruits:
    print(fruit)  # Output: apple banana cherry

# 4. Iterating Over a String
word = "Python"
for letters in word:
    print(letters)  # Output: P y t h o n

# 5. Using the range() Function
for num in range(1, 10, 2):  # Start=1, Stop=10 (exclusive), Step=2
    print(num)  # Output: 1 3 5 7 9

# 6. Using else with For Loop
for i in range(5):
    print(i)
    if i == 2 :
        break
else:
    print("Loop finished!")  # Output: 0 1 2 Loop finished!

# 7. Nested For Loop
for i in range(3):
    for j in range(2):
        for k in range(4):
            print(f"i={i}, j={j}, k={k}")

# 8. Breaking a Loop
print("Search 4 in the given range.")
for num in range(10):
    if num == 4:
        statement = "we have found the number."
        print(statement , num)  # Output: 0 1 2
        break
    print(num)  # Output: 0 1 2

# 9. Using Continue Statement
for num in range(5):
    if num == 2:
        continue
    print(num)  # Output: 0 1 3 4

# # 10. Assignment for Students
# print("Assignment:")
# print("1. Write a Python program to iterate through a list of numbers and print only even numbers.")
# print("2. Write a nested loop to print the multiplication table from 1 to 5.")
# print("3. Use a 'for' loop with 'else' to check if a number exists in a list.")
