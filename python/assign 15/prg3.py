# creating class
import math
class Circle:
    def __init__(self, radius,x, y):
        self.radius = radius
        self.x = x
        self.y = y
    
    def area(self):
        return math.pi*self.radius**2
    
    def perimeter(self):
        return math.pi*2*self.radius
    
    def circumference(self):
        return math.pi*2*self.radius
    
circle1 = Circle(13,14,77)
print(f"Area of circle: {circle1.area()}")
print(f"perimeter of circle: {circle1.perimeter()}")
print(f"circumference of circle: {circle1.circumference()}")