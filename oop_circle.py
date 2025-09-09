import sys

class Circle:
    units = 'cm'

    def __init__(self, radius, position=(0, 0)):
        self.radius = radius
        self.position = position

    def __str__(self):
        return f"I am a circle of size {self.radius}{self.units} located at {self.position}."


def main():
    # instantiate
    circle = Circle(radius=5)
    print(circle)
    circle.position = (30, -50)
    print(circle)
    circle.radius = 17
    print(str(circle))
    return 0


if __name__ == "__main__":
    sys.exit(main())