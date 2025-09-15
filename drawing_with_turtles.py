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

def draw_circle():
    time.sleep(2)
    pen = turtle.Turtle()
    if pen.isdown():
        pen.up()
    pen.goto(15, 28)
    pen.down()
    pen.begin_fill()
    pen.pencolor("red")
    pen.fillcolor("purple")
    pen.circle(60)
    pen.end_fill()
    pen.up()
    turtle.done()

def main():
    # draw_rectangle()
    draw_circle()
    return 0


if __name__ == "__main__":
    sys.exit(main())