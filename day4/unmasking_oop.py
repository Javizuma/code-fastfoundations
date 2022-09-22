import math
import os
import sys


class Circle:
    units = 'cm'  # all circles will have the same units

    def __init__(self, radius, position=(0, 0)):
        self.radius = radius  # each circle will have a particular radius
        self.position = position
        self.diameter = radius * 2
        self.area = math.pi  * (radius ** 2)

    def __str__(self):  # Python special methods
        return f"I am a circle of size {self.radius}{self.units} located at {self.position}, with an area of {self.area} {self.units}^2."


def area(circle):
    return math.pi * circle.radius ** 2


def arc_length(circle, angle, degrees=False):
    """Function to compute the arc length l for the angle provided"""

    if degrees==True:
        return math.pi * circle.radius * 2 * (angle / 360)
    if degrees==False:
        return  math.pi * circle.radius *2 * (angle / 2*math.pi )
    else:
        return print('The values introduced were not in the correct format')

def bounding_box(circle):
    """Function to compute the four values of the bounding box for a circle"""
    return(
        circle.position[0] - circle.radius,
        circle.position[1] - circle.radius,
        circle.position[0] + circle.radius,
        circle.position[1] + circle.radius
    )

class Rectangle:
    def __init__(self, width, height, position=(0, 0), fill = 'white', stroke = 'black'):
        self.width = width
        self.height = height
        self.position = position
        self.fill = fill
        self.stroke = stroke

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


class Canvas:
    def __init__(self,width,lenght ):
        self.width=width
        self.length=lenght

class Text:
    def __init__(self, text, position(0,0), colour = 'black' ):
        self.text= text



def main():
    small_circle = Circle(10)
    big_circle = Circle(50)

    print(small_circle)
    print(big_circle)

    # now we change units for all instances on the class
    Circle.units = 'pm'

    print(small_circle)
    print(big_circle)

    # but
    big_circle.units = 'hm'  # only change for the big_circle instance

    small_circle
    print(small_circle)
    print(big_circle)


    #canvas = Canvas(1200, 780)
    #canvas.mystery_method()
    #turtle.done()

    return os.EX_OK


if __name__ == '__main__':
    sys.exit(main())
