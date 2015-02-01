# Vak: Numerical Recipes
# Auteurs: Robin Klusman 10675671, Maico Timmerman 10542590
try:
    import matplotlib.pyplot as plt
    assert plt
    import numpy as np
    assert np
    from scipy import ndimage, misc
    assert ndimage, misc
except ImportError:
    print("Warning: could not import.")

import math
import random


def slope_field(phi):
    """
    Creates a slope field with 100 t and y values equally
    spaced from 0,0 to 2,2
    """

    for i in range(10):
        a = i * 2/9.
        for j in range(10):
            b = j * 2/9.
            get_line(phi, a, b, 0.1)


def random_field(phi):
    """
    Creates a slope field with 2000 random t and y values
    """

    for i in range(2000):
        a = 2 * random.random()
        b = 2 * random.random()
        get_line(phi, a, b, 0.1)


def get_line(phi, t, y, length):
    """
    Makes a line using the slope gotten from the function and the
    line-length that we give to it.
    """

    s = phi(t, y)      # Slope
    c = length / 2     # Half Line Length
    a = t              # t (x) Position
    b = y              # y Position

    dy = c * math.sin(math.atan(s))  # Goniometrics
    dx = math.sqrt(c**2-dy**2)       # Pythagoras

    x1 = a - dx
    y1 = b - dy
    x2 = a + dx
    y2 = b + dy

    plt.plot([x1, x2], [y1, y2], 'b-', linewidth=1)

    # print('Plotted line at ({}, {}), ({}, {})'.format(x1, y1, x2, y2))


if __name__ == "__main__":
    phi = lambda t, y: 1 - 2 * t * y
    slope_field(phi)

    print('Slope field plot.')
    print('Close this plot to move on to the random plot.')
    plt.show()

    random_field(phi)

    print('Random field plot.')
    plt.show()
