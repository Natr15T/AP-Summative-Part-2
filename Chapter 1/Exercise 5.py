# Initialize counter
count = 0

# Ask the user if they want to continue
response = input("Would you like to continue? (Y/N): ").strip().upper()

# Loop as long as the user enters 'Y'
while response == 'Y':
    count += 1
    response = input("Would you like to continue? (Y/N): ").strip().upper()

# Output the number of times the loop was executed
print(f"The loop was executed {count} time(s).")
