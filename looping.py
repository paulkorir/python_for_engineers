import sys


def main():
    number_list = [8, 3, 2, 6, 12, 3, 14, 332, 72, 9]
    for number in number_list:
        square = number ** 2
        print(square)
    return 0


if __name__ == '__main__':
    sys.exit(main())