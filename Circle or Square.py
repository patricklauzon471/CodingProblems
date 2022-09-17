# Given radius of a circle or a square
# Return true if circumference of circle greater than square perimeter
# Return false if vice versa

from cmath import sqrt


def circle_or_square(radius, area):
    circle = radius*3.14*2
    square = (area ** 0.5)*4

    if circle > square:
        return True
    else:
        return False


print(circle_or_square(2, 15))
