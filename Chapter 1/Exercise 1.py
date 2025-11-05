# Prompt user for name
print("Hello, user!")
name = input("What is your name?\n")

# Prompt user for age
age = input("What is your age?\n")

# Convert age to integer for calculation
age = int(age)

# Format name using title() and calculate length
formatted_name = name.title()
name_length = len(name.replace(" ", ""))  # excluding spaces

# Print details
print(f"It is good to meet you, {formatted_name}")
print("The length of your name is:")
print(name_length)
print(f"You will be {age + 1} in a year.")
