# 004_string_formatting.py
# Demonstrate different string formatting techniques in Python.

print("String Formatting Example")
print()

student_name = "Alex"
student_score = 95.6789

# --------------------------------------------------
# 1. F-string Formatting
# --------------------------------------------------

print("F-String Example:")
print(f"Student: {student_name} | Score: {student_score:.2f}")

# --------------------------------------------------
# 2. Use .format() Method
# --------------------------------------------------

print("\n.format() Example:")
print("Student: {} | Score: {:.2f}".format(student_name, student_score))

# --------------------------------------------------
# 3. Use Percent (%) Formatting
# --------------------------------------------------

print("\nPercent Formatting Example:")
print("Student: %s | Score: %.2f" % (student_name, student_score))

# --------------------------------------------------
# 4. Alignment Example Using F-strings
# --------------------------------------------------

print("\nAlignment Example: (using f-string)")

print("\nCode:")
print("\tprint(f\"{student_name:<10} | {student_score:>8.2f}\")")
print("\nOutput:")
print(f"{student_name:<10} | {student_score:>8.2f}")

# Alignment is also possible using .format() and % formatting.
# Please observe code sections 5 and 6 below.

# --------------------------------------------------
# 5. Alignment Example Using .format() Method
# --------------------------------------------------

print("\nAlignment Example: (using .format() method)")

print("\nCode:")
print("\tprint(\"{:<10} | {:>8.2f}\".format(student_name, student_score))")
print("\nOutput:")
print("{:<10} | {:>8.2f}".format(student_name, student_score))

# --------------------------------------------------
# 6. Alignment Example Using Percent (%) Formatting
# --------------------------------------------------

print("\nAlignment Example: (using % formatting)")

print("\nCode:")
print("\tprint(\"%-10s | %8.2f\" % (student_name, student_score))")
print("\nOutput:")
print("%-10s | %8.2f" % (student_name, student_score))
