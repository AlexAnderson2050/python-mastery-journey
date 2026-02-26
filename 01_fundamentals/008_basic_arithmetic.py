# 008_basic_arithmetic.py
# Demonstrate arithmetic operations with validation and defensive programming.

print("Basic Arithmetic Operations")
print()

# --------------------------------------------------
# 1. Collect User Input (With Validation)
# --------------------------------------------------

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Error: Please enter valid numeric values.")
    exit()

print()

# --------------------------------------------------
# 2. Perform Arithmetic Operations
# --------------------------------------------------

print("Results:")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

# Defensive check for division
if num2 != 0:
    print("Division:", num1 / num2)
    print("Floor Division:", num1 // num2)
    print("Modulus:", num1 % num2)
else:
    print("Division: Cannot divide by zero.")
    print("Floor Division: Undefined.")
    print("Modulus: Undefined.")

print("Exponentiation:", num1 ** num2)
print()

# --------------------------------------------------
# 3. Order of Operations Demonstration
# --------------------------------------------------

example1 = 2 + 3 * 4
example2 = (2 + 3) * 4

print("Order of Operations Example:")
print("2 + 3 * 4 =", example1)
print("(2 + 3) * 4 =", example2)

# --------------------------------------------------
# Summary
# --------------------------------------------------
# - Used float() for flexible numeric input.
# - Applied try/except for input validation.
# - Prevented division by zero using a guard clause.
# - Demonstrated all primary arithmetic operators.
# - Illustrated order of operations using parentheses.
# - Practiced defensive programming principles.
