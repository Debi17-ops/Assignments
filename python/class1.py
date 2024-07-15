def area_square(side_length):
    return side_length ** 2
side_length=float(input("enter the side of square:"))                                   #question 1
area=area_square(side_length)
print("the area of the square with length {} is {}".format(side_length,area))


import math
def gcd_numbers(num1,num2):
    return math.gcd(num1,num2)
num1=int(input("enter the first number:"))                                               #question 2 using math function 
num2=int(input("enter the second number:"))
gcd=gcd_numbers(num1,num2)
print("the gcd of {} and {} is {}".format(num1,num2,gcd))


import math
def circumference(d):
    return math.pi**d
d=float(input("enter the diameter of the circle:"))                                    #question 3 using math function
calculate_circumference=circumference(d)
print("The diameter and circumference of circle is {} and {}".format(d,circumference))

def distance(d1,d2):
    return abs(d1-d2)
d1=float(input("enter the first number:"))
d2=float(input("enter the second number:"))                                           #question 5
d=distance(d1,d2)
print("the distance between {} and {} is {}".format(d1,d2,d))


def gcd(a,b):
    while b!=0:
        temp=b
        b=a%b
        a=temp
    return a
print("enter two numbers:")                                                          #question 2 
num1=int(input())
num2=int(input())
res=gcd(num1,num2)
print("the gcd is ",res)

def opposite_face(face):
    if 1<=face<=6:
        return 7-face                                                                #question 4
    else:
        return "invalid face number"
input=int(input("enter a dice face number(1-6):"))
oppo=opposite_face(input)
print("the opposite face number is:{}".format(oppo))

def circle(d):
    circumference=3.14*d
    return(circumference)
radius=float(input("enter the radius of circle:"))                                     #question 3
circumference=circle(radius)
print("circumference of circle is{}".format(circumference))    
