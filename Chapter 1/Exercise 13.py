# Function to calculate the product of list values
def calculate_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

# Main program
num_list = [2, 3, 4, 5]  # Example list

# Call the function and get the product
result = calculate_product(num_list)

# Display the result
print(f"The product of the list values {num_list} is: {result}")
