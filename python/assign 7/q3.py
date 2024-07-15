import math

def valid_triangle(a, b, c):

    return a + b > c and a + c > b and b + c > a

def classify_triangle(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
            return "Right-angled and Isosceles"
        else:
            return "Isosceles"
    elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        return "Right-angled"
    else:
        return "Scalene"

def circumcenter(a, b, c):

    if a**2 + b**2 == c**2:
        return c / 2
    elif a**2 + c**2 == b**2:
        return b / 2
    elif b**2 + c**2 == a**2:
        return a / 2
    else:
        return -1


a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))


if valid_triangle(a, b, c):
    triangle_type = classify_triangle(a, b, c)
    print(f"The triangle is {triangle_type}")
    
    if "Right-angled" in triangle_type:
        radius = circumcenter(a, b, c)
        print(f"The radius of the circumcenter is: {radius}")
    else:
        print("-1")
else:
    print("The given sides do not form a valid triangle")
