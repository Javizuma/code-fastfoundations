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

    return  math.pi * circle.radius *2 * (angle / 2*math.pi )

def bounding_box(circle):
    """Function to compute the four values of the bounding box for a circle"""


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
