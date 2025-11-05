# Prompt user for the lengths of the three sides
a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

# Check if the sides satisfy the triangle inequality
if (a + b > c) and (a + c > b) and (b + c > a):
    print("These sides form a valid triangle.")
    
    # Optional: classify the triangle
    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or a == c or b == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"
    
    print(f"The triangle is {triangle_type}.")
else:
    print("These sides do NOT form a triangle.")
