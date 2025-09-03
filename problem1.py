# d_squared = ...

import sys

def main():
    # add your code here
    # A = (x1, y1, z1)
    x1 = float(input("x1: "))
    # B = (x2, y2, z2)
    x2 = float(input("x2: "))
    print(type(x1))
    d_squared = (x1 - x2 ) ** 2
    print(f"{d_squared = }")
    return 0


if __name__ == "__main__":
    sys.exit(main())