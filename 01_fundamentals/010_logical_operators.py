# 010_logical_operators.py
# Demonstrate logical operators in Python.

print("Logical Operators Example")
print()

# --------------------------------------------------
# 1. Basic Logical Operators
# --------------------------------------------------

a = True
b = False

print("a =", a)
print("b =", b)
print()

print("a and b :", a and b)
print("a or b  :", a or b)
print("not a   :", not a)
print()

# --------------------------------------------------
# 2. Logical Operators with Comparisons
# --------------------------------------------------

number = 15

print("number =", number)
print("Is number between 10 and 20?",
      number > 10 and number < 20)
print("Is number less than 5 or greater than 12?",
      number < 5 or number > 12)
print()

# --------------------------------------------------
# 3. Real-World Validation Example
# --------------------------------------------------

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Error: Please enter a valid integer.")
    exit()

print()

if age >= 0 and age <= 120:
    print("Valid age entered.")
else:
    print("Invalid age range.")

if not (age >= 18):
    print("You are under 18.")
else:
    print("You are 18 or older.")

# --------------------------------------------------
# Summary
# --------------------------------------------------
# - Demonstrated logical operators: and, or, not.
# - Combined logical operators with comparison expressions.
# - Used logical conditions in a real-world validation example.
# - Applied defensive programming using try/except.
# - Practiced writing readable multi-condition expressions.
