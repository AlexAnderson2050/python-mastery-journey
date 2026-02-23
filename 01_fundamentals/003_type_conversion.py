# Prompt the user for their name and age, then calculate and display their age next year.
user_name = input("What is your name? ")
user_age = int(input(f"How old are you, {user_name}? "))

next_year_age = user_age + 1

print(f"{user_name}, you will be {next_year_age} years old next year!")
