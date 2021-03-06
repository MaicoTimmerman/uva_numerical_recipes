# Vak: Numerical Recipes
# Auteurs: Robin Klusman 10675671, Maico Timmerman 10542590
try:
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy import ndimage, misc
    assert np
    assert plt
    assert ndimage, misc
except ImportError:
    print("Warning: could not import.")

import math
import random


def plot_slope_field(phi, fig=plt):
    """
    Creates a slope field with 100 t and y values equally
    spaced from 0,0 to 2,2
    """

    # For a grid of 10x10 from 0,0 to 2,2
    for i in range(10):

        # All points have exactly 2/9. distance from eachother.
        # 10 points have 9 spaces inbetween.
        a = i * 2/9.

        for j in range(10):
            b = j * 2/9.

            # Draw a line with given slope on location.
            x, y = get_line(phi, a, b, 0.1)
            plt.plot((x[0], x[1]), (y[0], y[1]), 'b-', linewidth=1)

    # Display the figure
    fig.show()


def plot_random_field(phi, fig=plt, t=None, y=None):
    """
    Creates a slope field with 2000 random t and y values
    Take in mind the domain and range. If none is given for a function,
    use the default range and domain of 2.
    """

    # Determine the domain (x values) of the function. If none, use default.
    if not t:
        x_min = 0
        x_max = 2
    else:
        x_min = min(t) - .25
        x_max = max(t) + .25

    # Determine the range (y values) of the function. If none, use default.
    if not t:
        y_min = 0
        y_max = 2
    else:
        y_min = min(y) - .25
        y_max = max(y) + .25

    # Generate 2000 random points lines, matching the given function.
    for i in range(2000):
        x = (random.random() * (x_max - x_min)) + x_min
        y = (random.random() * (y_max - y_min)) + y_min
        x, y = get_line(phi, x, y, 0.1)
        fig.plot((x[0], x[1]), (y[0], y[1]), 'b-', linewidth=1)

    if x_min and x_max and y_min and y_max:
        fig.xlim([x_min, x_max])
        fig.ylim([y_min, y_max])


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

    return ((x1, x2), (y1, y2))


if __name__ == "__main__":
    phi = lambda t, y: 1 - 2 * t * y

    print('Slope field plot.')
    plot_slope_field(phi)

    print('Random field plot.')
    plot_random_field(phi)
    plt.tight_layout()
    plt.show()
