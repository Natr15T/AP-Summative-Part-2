# Create the tuple
year = (2017, 2003, 2011, 2005, 1987, 2009, 2020, 2018, 2009)

# 1. Access the value at index -3
print(f"Value at index -3: {year[-3]}")

# 2. Reverse the tuple and print both original and reversed tuple
reversed_year = year[::-1]
print(f"Original tuple: {year}")
print(f"Reversed tuple: {reversed_year}")

# 3. Count the number of times 2009 appears
count_2009 = year.count(2009)
print(f"Number of times 2009 appears: {count_2009}")

# 4. Get the index of 2018
index_2018 = year.index(2018)
print(f"Index of 2018: {index_2018}")

# 5. Find the length of the tuple
tuple_length = len(year)
print(f"Length of the tuple: {tuple_length}")
