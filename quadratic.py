import cmath
import sys


def find_solutions(a, b, c):
    # discriminant
    d = b ** 2 - 4 * a * c
    print(f"discriminant = {d}")
    # roots:
    # x1 = (-b + math.sqrt(d)) / (2 * a)
    # x2 = (-b - math.sqrt(d)) / (2 * a)
    x1 = (-b + cmath.sqrt(d)) / (2 * a)
    x2 = (-b - cmath.sqrt(d)) / (2 * a)
    return x1, x2


def main():
    a = complex(input("a: "))
    b = complex(input("b: "))
    c = complex(input("c: "))
    x1, x2 = find_solutions(a, b, c)
    print("The roots are:")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
