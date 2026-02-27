# 012_while_loops.py
# Introduction to while loops in Python.

print("While Loops Exploration")
print()

# --------------------------------------------------
# 1. Basic while Loop
# --------------------------------------------------

print("Counting from 1 to 5:")

counter = 1

while counter <= 5:
    print(counter)
    counter += 1  # Important: update condition variable

print()

# --------------------------------------------------
# 2. Condition-Controlled Loop
# --------------------------------------------------

number = 3

while number > 0:
    print("Number is:", number)
    number -= 1

print("Loop finished because condition became False.")
print()

# --------------------------------------------------
# 3. Input Validation Loop (Defensive Programming)
# --------------------------------------------------

while True:
    try:
        user_number = int(input("Enter a positive number: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue

    if user_number > 0:
        break
    else:
        print("Number must be greater than 0.")

print("Valid number entered:", user_number)
print()

# --------------------------------------------------
# 4. Sentinel-Controlled Loop
# --------------------------------------------------

print("Type 'exit' to stop the program.")

while True:
    user_input = input("Enter something: ")

    if user_input.lower() == "exit":
        break

    print("You entered:", user_input)

print("Program ended.")

# --------------------------------------------------
# Summary
# --------------------------------------------------
# - Introduced the while loop structure.
# - Demonstrated counter-controlled repetition.
# - Showed how loop conditions control execution.
# - Applied defensive programming with input validation.
# - Used break and continue to control loop flow.
# - Demonstrated a sentinel-controlled loop pattern.
