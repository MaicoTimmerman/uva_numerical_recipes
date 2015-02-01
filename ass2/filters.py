# Vak: Numerical Recipes
# Auteurs: Robin Klusman 10675671, Maico Timmerman 10542590
try:
    import numpy as np
    assert np
except ImportError:
    print('Could not import numpy')


def prewitt():
    """returns x, and y Prewitt filter"""
    Px = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
    Py = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])

    return Px, Py


def laplace():
    """ Returns the Laplacian filter """

    return np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])


def sobel():
    """returns x, and y Sobel filter"""
    Sx = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
    Sy = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

    return Sx, Sy
