# 1. Create an integer list with 10 values
int_list = [34, 12, 56, 78, 23, 9, 45, 67, 31, 50]

# 2. Output the list using a for loop
print("Original list:")
for num in int_list:
    print(num, end=" ")
print("\n")

# 3. Output the highest and lowest value
print(f"Highest value: {max(int_list)}")
print(f"Lowest value: {min(int_list)}\n")

# 4. Sort the elements in ascending order
int_list.sort()
print("List in ascending order:")
print(int_list, "\n")

# 5. Sort the elements in descending order
int_list.sort(reverse=True)
print("List in descending order:")
print(int_list, "\n")

# 6. Append two elements
int_list.append(88)
int_list.append(15)

# 7. Print the list after appending
print("List after appending two elements:")
print(int_list)
