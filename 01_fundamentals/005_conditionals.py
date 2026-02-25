# Demonstrate conditional statements with clean structure.

print("Conditional Example:")
print()

try:
    student_score = int(input("Enter student score (0-100): "))

except ValueError:
    print("Error: Please enter a valid integer.")
    exit()

# Guard clause for range validation
if not 0 <= student_score <= 100:
    print("Error: Score must be between 0 and 100.")
    exit()

# Grade determination (no nesting needed anymore)
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
