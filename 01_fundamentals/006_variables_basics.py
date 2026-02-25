# Demonstrate the basics of variables in Python.

print("Variables Basics Example")
print()

# --------------------------------------------------
# 1. Variable Assignment
# --------------------------------------------------

# Assigning values to variables
name = "Alex"
age = 54
height = 1.75
is_student = True

print("Initial variable values:")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)
print()

# --------------------------------------------------
# 2. Reassignment
# --------------------------------------------------

# Variables can be reassigned
age = 55
print("After reassignment, Age:", age)
print()

# --------------------------------------------------
# 3. Dynamic Typing
# --------------------------------------------------

# A variable can change its type
value = 100
print("Value:", value, "| Type:", type(value))

value = "One Hundred"
print("Value:", value, "| Type:", type(value))
print()

# --------------------------------------------------
# 4. Multiple Assignment
# --------------------------------------------------

x, y, z = 10, 20, 30
print("Multiple assignment:")
print("x:", x, "y:", y, "z:", z)
print()

# --------------------------------------------------
# 5. User Interaction Example
# --------------------------------------------------

print("Now it's your turn.")
user_name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

current_year = 2026
calculated_age = current_year - birth_year

print()
print("Hello", user_name + "!")
print("You are approximately", calculated_age, "years old.")
