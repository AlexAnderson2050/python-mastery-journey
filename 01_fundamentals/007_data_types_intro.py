# 007_data_types_intro.py
# Introduction to basic data types in Python.

print("Data Types Introduction")
print()

# --------------------------------------------------
# 1. What Is a Data Type?
# --------------------------------------------------

print("A data type defines the kind of value a variable holds.")
print()

# --------------------------------------------------
# 2. Numeric Types
# --------------------------------------------------

integer_number = 10          # int
floating_number = 3.14       # float

print("Numeric Types:")
print("Integer value:", integer_number, "| Type:", type(integer_number))
print("Float value:", floating_number, "| Type:", type(floating_number))
print()

# --------------------------------------------------
# 3. Text Type
# --------------------------------------------------

text_value = "Hello, Python!"   # str

print("Text Type:")
print("String value:", text_value, "| Type:", type(text_value))
print()

# --------------------------------------------------
# 4. Boolean Type
# --------------------------------------------------

is_active = True   # bool

print("Boolean Type:")
print("Boolean value:", is_active, "| Type:", type(is_active))
print()

# --------------------------------------------------
# 5. Type Conversion (Preview)
# --------------------------------------------------

number_as_string = "25"
converted_number = int(number_as_string)

print("Type Conversion Example:")
print("Original value:", number_as_string, "| Type:", type(number_as_string))
print("Converted value:", converted_number, "| Type:", type(converted_number))
print()

# --------------------------------------------------
# 6. User Interaction Example
# --------------------------------------------------

print("Now it's your turn.")

user_input = input("Enter something: ")

print("You entered:", user_input)
print("Its data type is:", type(user_input))

# Summary:
# - Variables store values
# - Values have types
# - type() reveals the data type
