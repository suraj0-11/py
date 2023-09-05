import math


class Shape:
    def __init__(self):
        self.area = 0
        self.name = ""

    def showArea(self):
        print("The area of the", self.name, "is", self.area, "units")


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.name = "Circle"
        self.radius = radius

    def calcArea(self):
        self.area = math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__()
        self.name = "Rectangle"
        self.length = length
        self.breadth = breadth

    def calcArea(self):
        self.area = self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.name = "Triangle"
        self.base = base
        self.height = height

    def calcArea(self):
        self.area = self.base * self.height / 2

# print("---------------CIRCLE---------------")
# radius = int(input("Enter radius: "))
# print("---------------RECTANGLE---------------")
# length = int(input("Enter length: "))
# breadth = int(input("Enter breadth: "))
# print("---------------TRIANGLE---------------")
# base = int(input("Enter base: "))
# height = int(input("Enter height: "))

c1 = Circle(5)
c1.calcArea()
c1.showArea()

r1 = Rectangle(24,50)
r1.calcArea()
r1.showArea()

t1 = Triangle(3,5)
t1.calcArea()
t1.showArea()
