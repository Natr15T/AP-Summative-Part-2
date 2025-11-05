# Outer loop for the rows
for i in range(1, 6):
    # Inner loop for the numbers in each row
    for j in range(1, i + 1):
        print(j, end=" ")  # Print numbers on the same line
    print()  # Move to the next line after each row
