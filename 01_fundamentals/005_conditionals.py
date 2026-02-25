# 005_conditionals.py
# Demonstrate conditional statements with clean structure.

print("Conditional Example")
print()

# --------------------------------------------------
# 1. Catch Error Using try / except Commands
# --------------------------------------------------

try:
    student_score = int(input("Enter student score (0-100): "))

except ValueError:
    print("Error: Please enter a valid integer.")
    exit()

# --------------------------------------------------
# 2. Guard Clause for Range Validation
# --------------------------------------------------

if not 0 <= student_score <= 100:
    print("Error: Score must be between 0 and 100.")
    exit()

# --------------------------------------------------
# 3. Grade Determination
# --------------------------------------------------

if student_score >= 95:
    print("Grade: A")
elif student_score >= 85:
    print("Grade: B")
elif student_score >= 75:
    print("Grade: C")
elif student_score >= 65:
    print("Grade: D")
else:
    print("Grade: F")
