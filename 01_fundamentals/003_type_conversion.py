# 003_type_conversion.py
# Prompt the user for their name and age, then calculate and display their age next year.

print("Type Conversion Example")
print()

# --------------------------------------------------
# 1. Input User Name and Age
# --------------------------------------------------

user_name = input("What is your name? ")
user_age = int(input(f"How old are you, {user_name}? "))

# --------------------------------------------------
# 2. Calculate User Age in Next Year and Display It
# --------------------------------------------------

next_year_age = user_age + 1

print(f"{user_name}, you will be {next_year_age} years old next year!")

# --------------------------------------------------
# Summary
# --------------------------------------------------
# - Collected multiple inputs from the user.
# - Converted string input to integer using int().
# - Performed arithmetic on user-provided data.
# - Stored computed results in a new variable.
# - Reinforced the importance of data types in calculations.
