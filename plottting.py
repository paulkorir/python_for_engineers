import sys

import matplotlib.pyplot as plt
import numpy as np
import random


def plot_lines():
    x = np.linspace(0, 2 * np.pi, 200)
    print(f"{x = }")
    y = np.sin(x)
    print(f"{y = }")
    fig, ax = plt.subplots()
    print(f"{type(fig) = }; {type(ax) = }")
    ax.plot(x, y)
    plt.show()


def plot_scatter():
    x = [random.random() for _ in range(30)] # list comprehension
    y = [random.random() for _ in range(30)]
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    plt.show()

def plot_histogram():
    data = [random.gauss(0, 1) for _ in range(1000)] # N(0, 1)
    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(data, 20, density=True)
    plt.show()

def main():
    # plot_lines()
    # plot_scatter()
    return 0


if __name__ == '__main__':
    sys.exit(main())
