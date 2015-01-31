# Vak: Numerical Recipes
# Auteurs: Robin Klusman 10675671, Maico Timmerman 10542590
import numpy as np


def prewitt():
    """returns x, and y Prewitt filter"""
    Px = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
    Py = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])

    return Px, Py

# Here is room for other filers.. why not add them?
