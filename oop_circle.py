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

    def draw(self, pen):
        if pen.isdown():
            pen.up()
        x, y = self.position  # unpacking operation of a sequence type (list, tuple)
        pen.goto(x, y)
        pen.down()
        pen.begin_fill()
        pen.pencolor(self.stroke)
        pen.fillcolor(self.fill)
        pen.circle(self.radius)
        pen.end_fill()
        pen.up()


class Rectangle:
    def __init__(self, width, height, fill="white", stroke="black", stroke_width=1, opacity=1.0, position=(0, 0)):
        self.width = width
        self.height = height
        self.fill = fill
        self.stroke = stroke
        self.stroke_width = stroke_width
        self.opacity = opacity
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

    def draw(self, pen):
        if pen.isdown():
            pen.up()
        x, y = self.position
        pen.goto(x, y)
        pen.begin_fill()
        pen.pencolor(self.stroke)
        pen.fillcolor(self.fill)
        pen.forward(self.width)
        pen.right(90)  # 90 degree rotation
        pen.forward(self.height)
        pen.right(90)
        pen.forward(self.width)
        pen.right(90)
        pen.forward(self.height)
        pen.end_fill()
        pen.up()

    def __str__(self):
        return f"Rectangle: {self.width} * {self.height}"


class Triangle:
    def __init__(self):
        pass

    def draw(self, pen):
        pen.up()
        pen.goto(0, 0)
        pen.down()
        pen.forward(400)
        pen.left(90)
        pen.forward(300)
        pen.goto(0, 0)


class Canvas(turtle.TurtleScreen):
    def __init__(self, width: int = 1200, height: int = 750, bg: str = "white"):
        self.width = width
        self.height = height
        self.canvas = turtle.getcanvas()
        super().__init__(self.canvas)
        # fixed: the canvas is a turtle.TurtleScreen subclass so we can set the screensize on self
        self.screensize(width, height, bg)
        self.pen = turtle.RawPen(self.canvas)

    def mystery_method(self):
        self.pen.up()
        self.pen.goto(0, self.height / 2)  # what does this do
        self.pen.down()
        self.pen.goto(0, -self.height / 2)
        self.pen.up()
        self.pen.goto(-self.width / 2, 0)
        self.pen.down()
        self.pen.goto(self.width / 2, 0)
        self.pen.up()
        self.pen.home()

    def draw_circle(self, circle):
        # implement this
        if self.pen.isdown():
            self.pen.up()
        x, y = circle.position  # unpacking operation of a sequence type (list, tuple)
        self.pen.goto(x, y)
        self.pen.down()
        self.pen.begin_fill()
        self.pen.pencolor(circle.stroke)
        self.pen.fillcolor(circle.fill)
        self.pen.circle(circle.radius)
        self.pen.end_fill()
        self.pen.up()

    def draw_rectangle(self, rectangle):
        if self.pen.isdown():
            self.pen.up()
        x, y = rectangle.position
        self.pen.goto(x, y)
        self.pen.begin_fill()
        self.pen.pencolor(rectangle.stroke)
        self.pen.fillcolor(rectangle.fill)
        self.pen.forward(rectangle.width)
        self.pen.right(90)  # 90 degree rotation
        self.pen.forward(rectangle.height)
        self.pen.right(90)
        self.pen.forward(rectangle.width)
        self.pen.right(90)
        self.pen.forward(rectangle.height)
        self.pen.end_fill()
        self.pen.up()

    def draw(self, shape):  # generate shape
        # circle.draw(self.pen)
        shape.draw(self.pen)

    def write(self, text):
        text.write(self.pen)


class Text:
    def __init__(self, text, colour="red", align="center", font="Arial", position=(0, 0)):
        self.text = text
        self.position = position
        self.colour = colour
        self.align = align
        self.font = font

    def write(self, pen):
        pen.up()
        pen.goto(self.position[0], self.position[1])
        turtle.write(self.text, align=self.align, font=(self.font, 40, "normal"))


class Square(Rectangle):
    def __init__(self, width, *args, **kwargs):
        print(f"{args = }")
        print(f"{kwargs = }")
        super().__init__(width, width, *args, **kwargs)

    def __str__(self):  # overwritten the __str__ method
        return f"Square: {self.width} * {self.width}"

    def fake_method(self, a, b, c, d):  # four positional arguments
        print(f"{a = }, {b = }, {c = }, {d = }")

    def fake_method2(self, a=1, b=2, c=3, d=4):  # four keyword arguments
        print(f"{a = }, {b = }, {c = }, {d = }")


def composite_shape():
    """Composite shape"""
    shape = turtle.Shape("composite")
    shape.addcomponent(
        Square(
            width=100,
            colour="red",
            position=(20, 20)
        )
    )
    shape.addcomponent(
        Circle(
            200,
            colour="orange",
            position=(-100, -100)
        )
    )


def main():
    # instantiate
    circle = Circle(radius=80)
    # print(f"The area is {area(self)}")
    print(circle)
    circle.position = (30, -50)
    print(circle)
    # circle.radius = 17
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
    square = Square(width=5, opacity=0.5)
    print(square)
    print(f"{square.area() = }")
    print(f"{square.opacity = }")
    my_tuple = (1, 2, 3, 4)
    # print(f"{square.fake_method(1, 2, 3, 4) = }")
    square.fake_method(*my_tuple)

    my_dict = {'a': 5, 'b': 6, 'c': 7, 'd': 8}
    square.fake_method2(**my_dict)

    # canvas
    # canvas = Canvas()
    # canvas.mystery_method()
    # canvas.draw(circle)
    #
    # # draw the circle
    # # canvas.draw_circle(circle)
    #
    # # draw a rectangle
    # rect = Rectangle(150, 87, fill="blue", stroke="orange", position=(-250, 193))
    # # canvas.draw_rectangle(rect)
    # canvas.draw(rect)
    #
    # triangle = Triangle()
    # canvas.draw(triangle)
    #
    # text = Text("Hello world!", position=(-72, -67))
    # canvas.write(text)
    #
    # turtle.done()

    canvas = Canvas(1000, 700)
    gquad = Rectangle(
        200, 300, fill='#009a44', stroke='white', position=(-200, 300)
    )
    wquad = Rectangle(
        200, 300, fill='white', stroke='#dddddd', position=(0, 300)
    )
    oquad = Rectangle(
        200, 300, fill='#ff8200', stroke='white', position=(200, 300)
    )
    text = Text('IRELAND', position=(0, -250), align='center', font=('Arial', 60, 'bold'))
    canvas.draw(gquad)
    canvas.draw(wquad)
    canvas.draw(oquad)
    canvas.write(text)

    turtle.done()

    return 0


if __name__ == "__main__":
    sys.exit(main())
