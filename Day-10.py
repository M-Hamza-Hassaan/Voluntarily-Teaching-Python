# Python Strings Lesson

# 1. Introduction to Strings
# Strings are sequences of characters enclosed in quotes

str1 = 'Hello'
str2 = "Python"
str3 = '''This is a multi-line string'''

print("Introduction to Strings:")
print(str1)
print(str2)
print(str3)
print()

# 2. String Concatenation
# Using + operator to concatenate strings
name = input( "Enter your name: ") #got value from user,
greeting = f"Hello, {name}!" #concateniated and used the value
print("String Concatenation:")
print(greeting)  # Output: Hello, name!

# Using join() method to concatenate strings
words = ["1","2","3"]
# words = [1,2,3]
sentence = "".join(words)
print(sentence)  # Output: Hello Python Learners
print()
print(type(sentence))

# 3. f-Strings (Formatted Strings)
# f-Strings allow embedding expressions inside strings
name = "Alice"
age = 20
print("f-Strings (Formatted Strings):")
print(f"My name is {name} and I am {age} years old.")

# Performing calculations in f-Strings
a, b = 5, 10
print(f"Sum of {a} and {b} is {a + b}.")
print()

# 4. Accessing String Elements
# Strings are indexed, starting from 0

text = "Pythoninglify" #[P, y, t, h, o, n] 0 up to the last number - 1
print("Accessing String Elements:")
print(text[0])   # First character: P
print(text[-1])  # Last character: n
print(text[7])   # Third character: t
print()

# 5. Looping Through a String
# Loop through each character in a string
text = "Python"  #[P, y, t, h, o, n]
print("Looping Through a String:")
for char in text:
    print(char)

# Looping with index using enumerate()
for index, char in enumerate(text):
    print(f"Index : {index} + {char}")
print()

# 6. String Slicing
# Slicing strings to get parts of them
# text = "Python"  #[P, y, t, h, o, n]
# print("String Slicing:")
# print(text[0:6])   # Output: Python
# print(text[:6])    # Output: Python (same as above)
# print(text[7:])    # Output: Programming
# print(text[-3:])   # Output: ing
# print(text[::2])   # Output: Pto rgamn (every second character)
# print()

# # 7. String Methods
# # Some commonly used string methods
# text = "  Python Programming  "
# print("String Methods:")
# print(text.lower())     # Converts to lowercase
# print(text.upper())     # Converts to uppercase
# print(text.strip())     # Removes spaces from start and end
# print(text.replace("Python", "Java"))  # Replace words
# print(text.count("o"))  # Count occurrences of a character
# print(text.find("Prog"))  # Find index of a substring
# print(text.split())  # Splits string into a list of words
# print()

# Assignment 1: User's Full Name
print("Assignment 1:")
# 1. Write a program that takes a user's full name as input and prints:
# - The name in uppercase
# - The name in lowercase
# - The length of the name
# - The first and last characters of the name
# full_name = input("Enter your full name: ")
# print(f"Uppercase: {full_name.upper()}")
# print(f"Lowercase: {full_name.lower()}")
# print(f"Length of name: {len(full_name)}")
# print(f"First character: {full_name[0]}")
# print(f"Last character: {full_name[-1]}")
# print()

# # Assignment 2: Word Replacement and Counting
# print("Assignment 2:")
# # 2. Write a program that:
# # - Takes a sentence as input
# # - Counts the occurrences of a word given by the user
# # - Replaces that word with another word
# sentence = input("Enter a sentence: ")
# word_to_count = input("Enter a word to count: ")
# word_to_replace = input("Enter a word to replace it with: ")

# word_count = sentence.count(word_to_count)
# updated_sentence = sentence.replace(word_to_count, word_to_replace)

# print(f"Occurrences of '{word_to_count}': {word_count}")
# print(f"Updated sentence: {updated_sentence}")
