import sys
import turtle
import time
# turtle.forward()

# from turtle import *
# forward()


def draw_rectangle():
    turtle.forward(130)
    turtle.right(90)
    turtle.forward(110)
    turtle.right(90)
    turtle.forward(130)
    turtle.right(90)
    turtle.forward(110)
    turtle.done()

def draw_circle(radius=60):
    pen = turtle.Turtle()
    if pen.isdown():
        pen.up()
    pen.goto(15, 28)
    pen.down()
    pen.begin_fill()
    pen.pencolor("red")
    pen.fillcolor("purple")
    pen.circle(radius)
    pen.end_fill()
    pen.up()
    turtle.done()

def draw_triangle():
    turtle.forward(400)
    turtle.left(90)
    turtle.forward(300)
    turtle.goto(0, 0)
    turtle.done()

def write_text(text):
    turtle.penup()
    turtle.goto(20, 20)
    turtle.write(text, font=("Arial", 20, "normal"))
    turtle.done()


def main():
    # draw_rectangle()
    # draw_circle(180)
    # draw_triangle()
    write_text("Hello World")
    return 0


if __name__ == "__main__":
    sys.exit(main())