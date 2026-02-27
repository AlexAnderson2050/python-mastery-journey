# 013_for_loops.py
# Introduction to for loops in Python.

print("For Loops Exploration")
print()

# --------------------------------------------------
# 1. Basic for Loop with range()
# --------------------------------------------------

print("Counting from 0 to 4:")

for number in range(5):
    print(number)

print()

# --------------------------------------------------
# 2. range(start, stop)
# --------------------------------------------------

print("Counting from 1 to 5:")

for number in range(1, 6):
    print(number)

print()

# --------------------------------------------------
# 3. range(start, stop, step)
# --------------------------------------------------

print("Even numbers from 0 to 10:")

for number in range(0, 11, 2):
    print(number)

print()

# --------------------------------------------------
# 4. Looping Through a String
# --------------------------------------------------

word = "Python"

print("Characters in the word 'Python':")

for character in word:
    print(character)

print()

# --------------------------------------------------
# 5. Using break
# --------------------------------------------------

print("Stopping loop when number equals 5:")

for number in range(10):
    if number == 5:
        break
    print(number)

print("Loop stopped using break.")
print()

# --------------------------------------------------
# 6. Using continue
# --------------------------------------------------

print("Skipping number 3:")

for number in range(6):
    if number == 3:
        continue
    print(number)

print()

# --------------------------------------------------
# 7. Input Validation with for Loop (Defensive Programming)
# --------------------------------------------------

while True:
    user_input = input("Enter a positive integer (max 5): ")

    if not user_input.isdigit():
        print("Invalid input. Please enter digits only.")
        continue

    count = int(user_input)

    if count <= 0:
        print("Number must be greater than 0.")
        continue

    if count > 5:
        print("Number must not exceed 5.")
        continue

    break

print("Printing iterations:")

for i in range(count):
    print("Iteration", i + 1)

print()

# --------------------------------------------------
# Summary
# --------------------------------------------------
# - Introduced the for loop structure.
# - Used range() to generate number sequences.
# - Demonstrated start, stop, and step arguments.
# - Iterated over a string.
# - Used break to exit a loop early.
# - Used continue to skip an iteration.
# - Applied defensive programming for safe input handling.
