import math
import random
import time


def riemann_sum(f, a, b, n, method):
    """
    Riemann sum approximation of surface underneath a curve.
    Function f defines a curve, a is the left bound, b is the right bound.
    n is the amount of steps to take within the interval a, b.
    Method defines which type of Riemann sum we should use.
    """

    h = float(b - a) / n
    area = 0

    # Loop from 0 to n - 1 to take exactly n steps.
    for i in range(n):
        if method == 'left':
            x = a + i * h
        elif method == 'center':
            x = a + (i + .5) * h
        elif method == 'right':
            x = a + (i + 1) * h
        else:
            print('invalid method')
            area = float('NaN')
            break

        # Find the y of the function for this x, multiply it by the width (h)
        y = abs(f(x))
        area += y * h

    return area


def trapezoid_rule(f, a, b, n):
    """
    Trapezoid rule apporximation of the surface underneath a curve.
    Function f defines the curve, a is the left bound, b is the right bound.
    n is the amount of steps to take within the interval a, b.
    """

    h = float(b - a) / n
    area = 0

    # Loop from 0 to n - 1 to take exactly n steps.
    for i in range(n):
        # Left bound of trapezoid
        x_k = a + i * h
        # Right bound of trapezoid
        x_k1 = a + (i + 1) * h
        # Area of the trapezoid
        area += (abs(f(x_k)) + abs(f(x_k1))) * (h / 2)

    return area


def simpson_rule(f, a, b, n):
    """
    Simpson rule approximation of the surface underneath a curve.
    Function f defines a curve, a is the left bound, b is the right bound.
    n defines how many values for x within the interval a, b are used.
    """

    h = float(b - a) / n
    area = 0

    # We take steps of 2, since we use x + 1 as the middle point for the
    # approximation curve. x + 2 is used here as x_k2 and in the next iteration
    # as x_k.
    for i in range(0, n, 2):
        # Find the x value of the three poins we will be using.
        x_k = a + i * h
        x_k1 = a + (i + 1) * h
        x_k2 = a + (i + 2) * h

        # Find the area underneath the apporximation curve defined by the
        # three points.
        area += (abs(f(x_k)) + 4 * abs(f(x_k1)) + abs(f(x_k2))) * (h / 3)

    return area


def montecarlo(f, a, b, n):
    """
    Monte Carlo apporximation of the surface area underneath a curve.
    Function f defines a curve, a is the left bound, b is the right bound.
    n defines how many random points we plot for our apporximation.
    """

    # Stepsize for checking f for its maximum value, 0.01 fr decent precision.
    check_stepsize = 0.01

    # Find max y value of the graph.
    ymax = 0
    for i in range(int((b - a) * (1 / check_stepsize))):
        x = a + i * check_stepsize
        if abs(f(x)) > ymax:
            ymax = abs(f(x))

    # Round ymax to an integer value for easier calculation and add 1 just to
    # make sure the plane is bigger than any value the function produces.
    ymax = int(math.ceil(ymax) + 1)
    ymin = 0
    xmax = b
    xmin = a

    # Define a plane spanning from xmin (a), xmax (b), ymin, ymax. Generate
    # random points within this plane and count how any are below the graph
    # defined by f.
    matches = 0
    mismatches = 0
    random.seed(time.time())
    for i in range(n):
        x = xmin + random.random() * xmax
        y = ymin + random.random() * ymax

        # Abs so it also works for negative functions.
        if y <= abs(f(x)):
            matches += 1
        else:
            mismatches += 1

    # Use the total surface of the plane and the distribution of plotted
    # points to estimate the surface area underneath the curve.
    plane_surface = (xmax - xmin) * (ymax - ymin)
    area = matches / float(matches + mismatches) * plane_surface

    return area


def test_error_rieman(func, precision, method):

    # Start with 1 bar and keep increasing until the precision is met
    bars = 10000
    decimals = 1

    while(True):
        if (decimals == precision + 1):
            return
        if (round(riemann_sum(func, 0, 1, bars, method), decimals) ==
                round(math.pi, decimals)):
            print('n: %d for %d decimals' % (bars, decimals))
            decimals += 1
        bars += 1

if __name__ == "__main__":
    function1 = lambda x: 4 / float((pow(x, 2) + 1))
    function2 = lambda x: math.sin(x)

    print('-------RIEMANN-------')
    print(riemann_sum(function1, 0, 1, 100, 'left'))
    print(riemann_sum(function1, 0, 1, 100, 'center'))
    print(riemann_sum(function1, 0, 1, 100, 'right'))
    print(riemann_sum(function2, 0, math.pi, 100, 'left'))
    print(riemann_sum(function2, 0, math.pi, 100, 'center'))
    print(riemann_sum(function2, 0, math.pi, 100, 'right'))

    print('------TRAPEZOID------')
    print(trapezoid_rule(function1, 0, 1, 100))
    print(trapezoid_rule(function2, 0, math.pi, 100))

    print('-------SIMPSON-------')
    print(simpson_rule(function1, 0, 1, 100))
    print(simpson_rule(function2, 0, math.pi, 100))

    print('-----Monte Carlo-----')
    print(montecarlo(function1, 0, 1, 100000))
    print(montecarlo(function2, 0, math.pi, 100000))

    print('-----Test Efficiency------')
    print('Error val: 0.1')
    print('left:')
    test_error_rieman(function1, 4, method='left')
    print('center:')
    test_error_rieman(function1, 4, method='center')
    print('right:')
    test_error_rieman(function1, 4, method='right')
