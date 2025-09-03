import sys


def main():
    # user inputs values of a, b, c
    a = float(input("a: "))  # convert string to float
    b = float(input("b: "))
    c = float(input("c: "))
    # calculate the discriminant; we use operators for this
    discriminant = b ** 2 - 4 * a * c
    # output to user the value
    print(f"{discriminant = }")  # f-string (formatted string)
    return 0


if __name__ == "__main__":
    sys.exit(main())
