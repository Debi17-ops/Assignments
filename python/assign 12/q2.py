import random
import string

def random_char():
    return (random.choice(string.ascii_letters))


def random_string(length):
    return (" ".join(string.ascii_letters) for _ in range(length))


def string_fixed_length():
    fixed_length = 10       
    
    return (" ".join(string.ascii_letters) for _ in range(fixed_length))

res1 = random_char()
print(res1)

length = int(input("Enter the length of the string: "))         
res2 = random_string(length)
print(res2)

res3 = string_fixed_length()
print(res3)