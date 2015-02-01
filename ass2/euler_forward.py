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


def euler(phi, t0, y0, t1, n):
    """
    Get the graph approximation using euler method.
    """

    h = (t1 - t0) / float(n)
    t = t0
    y = y0
    tvals = []
    yvals = []
    for i in range(n):
        y += h * phi(t, y)
        t += h
        yvals.append(y)
        tvals.append(t)

    plt.plot(tvals, yvals, 'r-', linewidth=1)
    linefield.random_field(phi)


if __name__ == "__main__":
    f1 = lambda t, y: 1 - 2 * t * y
    f2 = lambda t, y: y * (1 - 1 / 3 * y)

    euler(f1, 0, 1.5, 2, 2000)
    euler(f1, 0, .25, 2, 2000)
    print('Euler for 1-2ty')
    print('Close this plot for next plot.')
    plt.show()

    euler(f2, -1, .25, 1, 2000)
    euler(f2, -1, 2.5, 1, 2000)
    print('Euler for y(1-1/3y)')
    plt.show()
