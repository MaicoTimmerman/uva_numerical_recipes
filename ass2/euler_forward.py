# Vak: Numerical Recipes
# Auteurs: Robin Klusman 10675671, Maico Timmerman 10542590
try:
    import matplotlib.pyplot as plt
    assert plt
except ImportError:
    print("Warning: could not import matplotlib.pyplot")
try:
    import numpy as np
    assert np
except ImportError:
    print("Warning: could not import numpy")
try:
    from scipy import ndimage, misc
    assert ndimage, misc
except ImportError:
    print("Warning: could not import scipy.ndimage")

import linefield


def euler(phi, t0, y0, t1, n, color):
    """
    Get the graph approximation using euler method.
    """

    h = (t1 - t0) / float(n)  # Step width
    t = t0                    # Start t
    y = y0                    # Start y
    tvals = []                # Array of t values
    yvals = []                # Array of y values

    for i in range(n):
        y += h * phi(t, y)
        t += h
        yvals.append(y)
        tvals.append(t)

    linefield.random_field(phi)
    plt.plot(tvals, yvals, color, linewidth=2)


if __name__ == "__main__":
    f1 = lambda t, y: 1 - 2 * t * y
    f2 = lambda t, y: y * (1 - 1 / 3 * y)

    euler(f1, 0, 1.5, 2, 2000, 'r-')
    euler(f1, 0, .25, 2, 2000, 'm-')
    print('Euler for 1-2ty')
    print('Close this plot for next plot.')
    plt.show()

    euler(f2, -1, .25, 1, 2000, 'r-')
    euler(f2, -1, 2.5, 1, 2000, 'm-')
    print('Euler for y(1-1/3y)')
    plt.show()
