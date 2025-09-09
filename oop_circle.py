import math
import sys


class Circle:
    units = 'cm'

    def __init__(self, radius, position=(0, 0)):
        self.radius = radius
        self.position = position
        # create two attributes 'diameter' and 'area'
        self.diameter = 2 * radius
        self.area = 3.142 * self.radius * self.radius

    def __str__(self):
        return f"I am a circle of size {self.radius}{self.units} located at {self.position}."


def area(circle):
    return math.pi * circle.radius ** 2


def perimeter(circle):
    return 2 * math.pi * circle.radius


def arc_length(circle, theta, radians=True):
    if radians:
        return theta * circle.radius
    else:
        theta_radians = math.radians(theta)
        return theta_radians * circle.radius


def bounding_box(circle):
    xmin = circle.position[0] - circle.radius
    xmax = circle.position[0] + circle.radius
    ymin = circle.position[1] - circle.radius
    ymax = circle.position[1] + circle.radius
    return xmin, ymin, xmax, ymax


def main():
    # instantiate
    circle = Circle(radius=5)
    print(f"The area is {area(circle)}")
    print(circle)
    circle.position = (30, -50)
    print(circle)
    circle.radius = 17
    print(str(circle))
    print(f"My diameter is {circle.diameter}{circle.units}.")
    print(f"My area is {circle.area}{circle.units}^2.")

    # function that calculates area
    print(f"The area is {area(circle)}")

    # perimeter
    print(f"{perimeter(circle) = }")
    # arc length
    print(f"{arc_length(circle, 0.8) = }")

    # bounding box
    print(f"{bounding_box(circle) = }")
    return 0


if __name__ == "__main__":
    sys.exit(main())
