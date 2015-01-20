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
    Trapezoid rule approximation of the surface underneath a curve.
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


def test_error_riemann(func, val, interval, precision, method):
    """
    Test the needed number of bars voor a specified precision. With precision
    being equal to the total number of digits after the decimal point. The
    method defines if the left, right or center riemann sum is taken. Val is
    the exact value the function should take
    """

    # Start with 1 bar and keep increasing until the precision is met
    bars = 1
    decimals = 1

    while(True):
        if (decimals == precision + 1):
            return
        if (round(riemann_sum(func, 0, interval, bars, method), decimals) ==
                round(val, decimals)):
            print('n: %d for %d decimals' % (bars, decimals))
            decimals += 1
        bars += 1


def test_error_func(method, func, interval, val, precision):
    """
    The integration method precision is tested on the func. The precision is
    equal to the number of digits after the decimal point. The val is the exact
    value the method should take.
    """

    # Start with 1 and keep increasing until the precision is met
    n = 30000
    decimals = 7

    while(True):
        if (decimals == precision + 1):
            print('stop')
            return
        if (round(method(func, 0, interval, n), decimals) ==
                round(val, decimals)):
            print('n: %d for %d decimals' % (n, decimals))
            decimals += 1
        n += 1
        if ((n % 1000) == 0):
            print('n: %d' % n)


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
    # print('Riemann_sum (4/pow(x, 2) + 1)')
    # print('left:')
    # test_error_riemann(function1, math.pi, interval, 4, method='left')
    # print('center:')
    # test_error_riemann(function1, math.pi, interval, 4, method='center')
    # print('right:')
    # test_error_riemann(function1, math.pi, interval, 4, method='right')

    # print('Riemann sum sin')
    # print('left:')
    # test_error_riemann(math.sin, 2, math.pi, 7, method='left')
    # print('center:')
    # test_error_riemann(math.sin, 2, math.pi, 7, method='center')
    # print('right:')
    # test_error_riemann(math.sin, 2, math.pi, 7, method='right')
    print('montecarlo')
    test_error_func(montecarlo, math.sin, math.pi, 2, 7)
    # print('simpson_rule')
    # test_error_func(simpson_rule, math.sin, math.pi, 2, 7)
    # print('trapezoid_rule')
    # test_error_func(trapezoid_rule, math.sin, math.pi, 2, 7)
