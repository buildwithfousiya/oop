#Polymorphism:
#One thing having many forms; the same function name can work differently for different objects.

#1)overriding
class Shape:
    def perimeter(self):
        print("test")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

def print_perimeter(Shape):
    print(f"The perimeter is: {Shape.perimeter()}")

circle = Circle(5)
rectangle = Rectangle(3, 6)

# print_perimeter(circle)
# print_perimeter(rectangle)

#2)overloading

class Operation:
    def sum(self, num1=0, num2=0, num3=0, num4=0):
        res = num1 + num2 + num3 + num4
        print(f"Result: {res}")

s1 = Operation()
s1.sum()
s1.sum(1, 2)
s1.sum(1, 2, 3)
s1.sum(1, 2, 3, 4)
