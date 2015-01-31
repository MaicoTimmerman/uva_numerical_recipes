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


def euler(phi, t0, y0, t1, n):
    """
    Args:
        phi (func pointer) - is de functie bij de GDV dy/dt = phi(t,y)
        beginwaarde(float) - y(t0) = y0 tijdinterval is [t0, t1]
        n(int) - is het aantal stappen in de EUler metode
        t(np.array) - is de numpy array van tijdstippen
        y(np.array) - is de numpy array van berekende functiewaarden
    """
    # return t, y
    pass


if __name__ == "__main__":
    pass
