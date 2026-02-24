# Demonstrate different string formatting techniques in Python.

student_name = "Alex"
student_score = 95.6789

# 1. f-string formatting
print("F-String Example:")
print(f"Student: {student_name} | Score: {student_score:.2f}")

# 2. .format() method
print("\n.format() Example:")
print("Student: {} | Score: {:.2f}".format(student_name, student_score))

# 3. Percent (%) formatting
print("\nPercent Formatting Example:")
print("Student: %s | Score: %.2f" % (student_name, student_score))

# 4. Alignment example using f-strings
print("\nAlignment Example: (using f-string)")

print("\nCode:")
print("\tprint(f\"{student_name:<10} | {student_score:>8.2f}\")")
print("\nOutput:")
print(f"{student_name:<10} | {student_score:>8.2f}")

# Alignment is also possible using .format() and % formatting.
# Please observe code sections 5 and 6 below.

# 5. Alignment example using .format() method
print("\nAlignment Example: (using .format() method)")

print("\nCode:")
print("\tprint(\"{:<10} | {:>8.2f}\".format(student_name, student_score))")
print("\nOutput:")
print("{:<10} | {:>8.2f}".format(student_name, student_score))

# 6. Alignment example using percent (%) formatting
print("\nAlignment Example: (using % formatting)")

print("\nCode:")
print("\tprint(\"%-10s | %8.2f\" % (student_name, student_score))")
print("\nOutput:")
print("%-10s | %8.2f" % (student_name, student_score))
