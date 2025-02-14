"""
Day 7
"""
# Lesson: Loops in Python
# kab start hoga..... kab end hoga 
# 1. For Loop

print("For Loop Example:")

for i in range(1, 6):  # Loops from 1 to 5
    print(f"Iteration {i}")

print("\n")

# 2. While Loop
print("While Loop Example:")
n = 1
while n <= 5:
    print(f"Iteration {n}")
    n += 1

print("\n")

# 3. Nested Loops
print("Nested Loop Example:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"(i={i}, j={j})", end=" ")
    print()  # Newline after inner loop

print("\n")

# 4. Loop with Break and Continue
print("Loop with Break and Continue:")
for i in range(1, 6):
    if i == 3:
        print("Skipping iteration 3 using continue.")
        continue
    if i == 5:
        print("Stopping loop at iteration 5 using break.")
        break
    print(f"Iteration {i}")

print("\n")

# Assignment:
# 1. Write a Python program using a for loop to print even numbers from 1 to 20.
# 2. Use a while loop to print the first 10 multiples of 3.
# 3. Create a nested loop to print the following pattern:
#    *
#    **
#    ***
#    ****
#    *****