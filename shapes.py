import math
import sys
import turtle

import numpy as np


def compute_ellipse_points(x, width, height, granularity, position=(0.0, 0.0)):
    """Compute a point on an ellipse given the x coordinate, width, and height."""
    a = width / 2.0
    b = height / 2.0
    top_points = list()
    bottom_points = list()
    for x in np.linspace(-width / 2, width / 2, num=granularity):
        discr = 1 - x ** 2 / a ** 2
        print(f"{discr:.3f}")
        y1 = b * math.sqrt(discr)
        y2 = -b * math.sqrt(discr)
        top_points.append((x, y1))
        bottom_points.append((x, y2))
        print(f"x: {x}, y1: {y1}, y2: {y2}")
    ellipse_points_at_origin = np.array(top_points + bottom_points[::-1])
    ellipse_points = ellipse_points_at_origin + np.array(position)
    return ellipse_points


def default_input(prompt="", default=None, return_type=None):
    """Substitute method for input() that has a default value and return type

     Usage:
        var = default_input(prompt, default=0.0, return_type=float)

    The above will print the prompt then allow a user to skip by pressing enter to return the specified default value
     """
    val = input(prompt)
    if val == "":
        return default
    if return_type is None:
        return val
    return return_type(val)


def draw_ellipse(points):
    """Draw an ellipse given the points. Points can be any sequence with pair of floats"""
    pen = turtle.Pen()
    if pen.isdown():
        pen.up()
    pen.goto(*points[-1])
    pen.down()
    for point in points:
        pen.goto(*point)
    turtle.done()


def main():
    width = float(input("ellipse width: "))  # must be positive
    height = float(input("ellipse height: "))  # must be positive
    granularity_str = input("ellipse granularity [default=20]: ")
    granularity = int(granularity_str) if granularity_str != "" else 20
    default_position = 0.0
    position_x = default_input(f"ellipse position x [default={default_position}]: ", default_position,
                               return_type=float)
    position_y = default_input(f"ellipse position y [default={default_position}]: ", default_position,
                               return_type=float)
    ellipse_points = compute_ellipse_points(width, width, height, granularity, position=(position_x, position_y))
    print(f"ellipse points: {ellipse_points}")

    # draw the ellipse
    draw_ellipse(ellipse_points)
    return 0


if __name__ == '__main__':
    sys.exit(main())
