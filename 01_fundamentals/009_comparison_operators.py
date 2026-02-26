# 009_comparison_operators.py
# Demonstrate comparison operators in Python.

print("Comparison Operators Example")
print()

# --------------------------------------------------
# 1. Basic Comparisons
# --------------------------------------------------

a = 10
b = 5

print("a =", a)
print("b =", b)
print()

print("a == b :", a == b)   # Equal to
print("a != b :", a != b)   # Not equal to
print("a > b  :", a > b)    # Greater than
print("a < b  :", a < b)    # Less than
print("a >= b :", a >= b)   # Greater than or equal to
print("a <= b :", a <= b)   # Less than or equal to
print()

# --------------------------------------------------
# 2. Chained Comparisons
# --------------------------------------------------

number = 15

print("Chained Comparison Example:")
print("10 < number < 20 :", 10 < number < 20)
print()

# --------------------------------------------------
# 3. User Interaction Example
# --------------------------------------------------

try:
    user_number = float(input("Enter a number: "))
except ValueError:
    print("Error: Please enter a valid number.")
    exit()

print()

print("Is the number positive?", user_number > 0)
print("Is the number negative?", user_number < 0)
print("Is the number zero?", user_number == 0)

# --------------------------------------------------
# Summary
# --------------------------------------------------
# - Demonstrated all primary comparison operators.
# - Showed that comparisons return Boolean values (True/False).
# - Introduced chained comparisons for readability.
# - Applied defensive programming using try/except.
# - Used comparisons in a real-world input scenario.
