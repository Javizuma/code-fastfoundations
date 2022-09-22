import math


class Rectangle:
    def __init__(self, width, height, position=(0, 0)):
        self.width = width
        self.height = height
        self.position = position

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.width)

    def diagonal(self):
        return math.sqrt(self.width**2 + self.height**2)

    def bounding_box(self):
        return(   circle.position[0] - rectangle.radius,
        circle.position[1] - rectangle.radius,
        circle.position[0] + rectangle.radius,
        circle.position[1] + rectangle.radius
        )
