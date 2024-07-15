import math

def perfect_square(number):
    if number < 0:
        return False
    root = math.isqrt(number)
    return root * root == number

input_number = int(input("Enter a number: "))

if perfect_square(input_number):
    print(f"{input_number} is a perfect square.")
else:
    print(f"{input_number} is not a perfect square.")
