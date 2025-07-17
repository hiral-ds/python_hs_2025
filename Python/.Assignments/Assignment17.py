#polymorphism

import math

class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

shapes = [
    Circle(5),
    Rectangle(4, 6),
    Circle(2.5),
    Rectangle(10, 3)
]

for shape in shapes:
    print(f"{type(shape).__name__} Area: {shape.area():.2f}")