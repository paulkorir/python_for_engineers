import math
import sys


class Circle:
    units = 'cm'

    def __init__(self, radius, position=(0, 0)):
        self.radius = radius
        self.position = position
        # create two attributes 'diameter' and 'area'
        self.diameter = 2 * radius
        # self.area = 3.142 * self.radius * self.radius

    def __str__(self):
        return f"I am a circle of size {self.radius}{self.units} located at {self.position}."

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def arc_length(self, theta, radians=True):
        if radians:
            return theta * self.radius
        else:
            theta_radians = math.radians(theta)
            return theta_radians * self.radius

    def bounding_box(self):
        xmin = self.position[0] - self.radius
        xmax = self.position[0] + self.radius
        ymin = self.position[1] - self.radius
        ymax = self.position[1] + self.radius
        return xmin, ymin, xmax, ymax


def main():
    # instantiate
    circle = Circle(radius=5)
    # print(f"The area is {area(self)}")
    print(circle)
    circle.position = (30, -50)
    print(circle)
    circle.radius = 17
    print(str(circle))
    print(f"My diameter is {circle.diameter}{circle.units}.")
    print(f"My area is {circle.area}{circle.units}^2.")

    # function that calculates area
    print(f"The area is {circle.area()}")

    # perimeter
    print(f"{circle.perimeter() = }")
    # arc length
    print(f"{circle.arc_length(0.8) = }")

    # bounding box
    print(f"{circle.bounding_box() = }")
    return 0


if __name__ == "__main__":
    sys.exit(main())
