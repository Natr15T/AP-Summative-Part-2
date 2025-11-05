# Prompt the user for two integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Perform calculations
sum_result = num1 + num2
diff_result = num1 - num2
product_result = num1 * num2
quotient_result = num1 / num2  # float division
remainder_result = num1 % num2

# Display results
print(f"\nSum (+): {sum_result}")
print(f"Difference (-): {diff_result}")
print(f"Product (x): {product_result}")
print(f"Quotient (/): {quotient_result}")
print(f"Remainder (%): {remainder_result}")
