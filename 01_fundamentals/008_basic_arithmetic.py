# 008_basic_arithmetic.py
# Demonstrate basic arithmetic operations in Python.

print("Basic Arithmetic Operations")
print()

# --------------------------------------------------
# 1. Basic Operators
# --------------------------------------------------

a = 10
b = 3

print("Given values:")
print("a =", a)
print("b =", b)
print()

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division (float):", a / b)
print("Floor Division:", a // b)
print("Modulus (remainder):", a % b)
print("Exponentiation:", a ** b)
print()

# --------------------------------------------------
# 2. Order of Operations
# --------------------------------------------------

result = 2 + 3 * 4
print("2 + 3 * 4 =", result)

result_with_parentheses = (2 + 3) * 4
print("(2 + 3) * 4 =", result_with_parentheses)
print()

# --------------------------------------------------
# 3. User Interaction Example
# --------------------------------------------------

print("Now it's your turn.")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print()
print("Results:")
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)

if num2 != 0:
    print("Quotient:", num1 / num2)
else:
    print("Cannot divide by zero.")

# --------------------------------------------------
# Summary
# --------------------------------------------------
# - Demonstrated all core arithmetic operators (+, -, *, /, //, %, **).
# - Explained difference between division and floor division.
# - Demonstrated order of operations (PEMDAS principle).
# - Used float() for flexible numeric input.
# - Included safe division check to prevent division by zero.
