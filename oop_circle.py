import math
import sys
import turtle


class Circle:
    units = 'cm'

    def __init__(self, radius, fill="white", stroke="black", position=(0, 0)):
        self.radius = radius
        self.position = position
        self.fill = fill
        self.stroke = stroke
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
        x_min = self.position[0] - self.radius
        x_max = self.position[0] + self.radius
        y_min = self.position[1] - self.radius
        y_max = self.position[1] + self.radius
        return x_min, y_min, x_max, y_max


class Rectangle:
    def __init__(self, width, height, fill="white", stroke="black", stroke_width=1, position=(0, 0)):
        self.width = width
        self.height = height
        self.fill = fill
        self.stroke = stroke
        self.stroke_width = stroke_width
        self.position = position

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    def bounding_box(self):
        x_min = self.position[0] - self.width / 2
        x_max = self.position[0] + self.width / 2
        y_min = self.position[1] - self.height / 2
        y_max = self.position[1] + self.height / 2
        return x_min, y_min, x_max, y_max

    def diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)

    def __str__(self):
        return f"Rectangle: {self.width} * {self.height}"


class Canvas(turtle.TurtleScreen):
    def __init__(self, width=1200, height=750, bg="white"):
        self.width = width
        self.height = height
        self.canvas = turtle.getcanvas()
        super().__init__(self.canvas)
        turtle.screensize(width, height, bg)
        self.pen = turtle.RawPen(self.canvas)

    def mystery_method(self):
        self.pen.up()
        self.pen.goto(0, self.height / 2) # what does this do
        self.pen.down()
        self.pen.goto(0, -self.height / 2)
        self.pen.up()
        self.pen.goto(-self.width / 2, 0)
        self.pen.down()
        self.pen.goto(self.width / 2, 0)
        self.pen.up()
        self.pen.home()


class Text:
    def __init__(self, text, colour="red", position=(0, 0)):
        self.text = text
        self.position = position
        self.colour = colour


# class Square:
#     def __init__(self, width, fill="white", stroke="black", position=(0, 0)):
#         self.width = width
#         self.fill = fill
#         self.stroke = stroke
#         self.position = position
#
#     def area(self):
#         return self.width ** 2
#
#     def __str__(self):
#         return f"Square: {self.width} * {self.width}"


class Square(Rectangle):
    def __init__(self, width, *args, **kwargs):
        super().__init__(width, width, *args, **kwargs)

    def __str__(self): # overwritten the __str__ method
        return f"Square: {self.width} * {self.width}"


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

    # instantiate a square object
    square = Square(width=5)
    print(square)
    print(f"{square.area() = }")

    # canvas
    canvas = Canvas()
    canvas.mystery_method()

    return 0


if __name__ == "__main__":
    sys.exit(main())
