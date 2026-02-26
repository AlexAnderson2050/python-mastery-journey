# 011_if_statements.py
# Explore different forms of if statements in Python.

print("If Statements Exploration")
print()

# --------------------------------------------------
# 1. Simple if Statement
# --------------------------------------------------

number = 10

print("Number:", number)

if number > 0:
    print("The number is positive.")

print()

# --------------------------------------------------
# 2. if / else Structure
# --------------------------------------------------

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

print()

# --------------------------------------------------
# 3. if / elif / else Structure
# --------------------------------------------------

score = 82

print("Score:", score)

if score >= 95:
    print("Grade: A")
elif score >= 85:
    print("Grade: B")
elif score >= 75:
    print("Grade: C")
elif score >= 65:
    print("Grade: D")
else:
    print("Grade: F")

print()

# --------------------------------------------------
# 4. Nested if Statement
# --------------------------------------------------

age = 20
has_id = True

print("Age:", age)
print("has_id:", has_id)

if age >= 18:
    if has_id:
        print("Entry allowed.")
    else:
        print("ID required for entry.")
else:
    print("You must be at least 18.")

print()

# --------------------------------------------------
# 5. Compound Condition (Cleaner Alternative)
# --------------------------------------------------

if age >= 18 and has_id:
    print("Entry allowed (compound condition).")
else:
    print("Entry denied (compound condition).")

# --------------------------------------------------
# Summary
# --------------------------------------------------
# - Demonstrated simple if statements.
# - Used if / else for binary decisions.
# - Used if / elif / else for multi-branch logic.
# - Compared nested if statements with compound conditions.
# - Practiced writing clearer, flatter conditional logic.
# - Reinforced logical operators inside condition checks.
