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
    print("Warning: could not import scipy, numpy or matplotlib.pyplot")

import linefield


def euler(phi, t0, y0, t1, n):
    """
    Get the graph approximation using euler method.

    phi is the function of the GDV dy/dt = phi(t,y)
    starting value y(t0) = y0
    timeinterval is [t0, t1]
    n is the number of steps in the euler method.
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

    return tvals, yvals


if __name__ == "__main__":
    f1 = lambda t, y: 1 - 2 * t * y
    f2 = lambda t, y: y * (1 - (1 / 3.) * y)

    # Euler for 1-2ty, with y(0) = 1.5
    t0, y0 = euler(f1, 0, 1.5, 2, 2000)

    # Euler for 1-2ty, with y(0) = .25
    t1, y1 = euler(f1, 0, .25, 2, 2000)

    # Plot a random linefield, with the two functions
    linefield.plot_random_field(f1, t=t0+t1, y=y0+y1)
    plt.plot(t0, y0, 'r-', linewidth=3)
    plt.plot(t1, y1, 'm-', linewidth=3)
    plt.show()

    # Euler for y-(1/3)*y*y)', with y(0) = .25
    t2, y2 = euler(f2, -1, .25, 1, 2000)

    # Euler for y-(1/3)*y*y)', with y(0) = 2.5
    t3, y3 = euler(f2, -1, 2.5, 1, 2000)

    # Plot a random linefield, with the two functions
    linefield.plot_random_field(f2, t=t2+t3, y=y2+y3)
    plt.plot(t2, y2, 'r-', linewidth=3)
    plt.plot(t3, y3, 'm-', linewidth=3)
    plt.show()
