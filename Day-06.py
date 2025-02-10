
# 5. Short-hand if statement

age = 18
if age >= 18: print("You are eligible to vote")

# # 6. Short-hand if-else (Ternary operator)
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)

# 7. Multiple short-hand conditions
marks = 75
result = "Passed" if marks >= 40 else "Failed"
print("Result:", result)

# 8. Logical operators with conditions
has_passport = input("has_passport- True or False:").strip().lower() == "true"
has_visa = input("has_visa- True or False:").strip().lower() == "true"
are_student = input("are_student- True or False:").strip().lower() == "true"

if has_passport and has_visa and are_student:
    print("You can travel internationally")
    print("You must travel for education")

elif has_passport and not are_student:
    print("You need a visa to travel")
else:
    print("You cannot travel internationally")


# ----Practice-------------

# Write a program that checks whether a user is eligible for a discount at a store. Ask the user:

# "Are you a student? (yes/no)"
# "Do you have a membership card? (yes/no)"
# Apply the following logic:

# If they are a student or have a membership, print "You are eligible for a discount!"
# Otherwise, print "No discount available."