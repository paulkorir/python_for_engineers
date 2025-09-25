import random
import sys

import matplotlib.pyplot as plt
import numpy as np


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
    x = [random.random() for _ in range(30)]  # list comprehension
    y = [random.random() for _ in range(30)]
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    plt.show()


def plot_histogram():
    data = [random.gauss(0, 1) for _ in range(1000)]  # N(0, 1)
    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(data, 20, density=True)
    plt.show()


def plot_multiplots_and_export():
    x = [random.random() for _ in range(30)]  # list comprehension
    y = [random.random() for _ in range(30)]
    data = [random.gauss(0, 1) for _ in range(1000)]  # N(0, 1)
    fig, ax = plt.subplots(1, 2)
    ax[0].scatter(x, y)
    ax[1].hist(data)
    plt.show()
    fig.savefig("plot.png")
    plt.close(fig)


def plot_legend():
    x = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(x)
    z = np.cos(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, label="sin(x)")
    ax.plot(x, z, label="cos(x)")
    ax.legend()
    ax.set_title('Plot Title')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True, linestyle='-.')
    ax.tick_params(axis='y', labelcolor='r', labelsize='medium', width=3)
    ax.set_xlim(6, 0)
    ax.axhline(0, color='black', linewidth=2)
    plt.show()


def main():
    # plot_lines()
    # plot_scatter()
    # plot_histogram()
    # plot_multiplots_and_export()
    plot_legend()
    return 0


if __name__ == '__main__':
    sys.exit(main())
