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


def show_images(images, cm=plt.cm.gray, axis='off'):
    """
    Shows an array of images in a figure-sublot

    Args:
        img(list) - list of images

    Optional:
        cm(plt.cm) - maptlotlib colormap
        axis(str) - argument to give plt
    """

    number_images = len(images)
    fig = plt.figure()

    for i, img in enumerate(images):
        fig.add_subplot(1, number_images, i)
        plt.axis(axis)
        plt.imshow(img, cmap=cm)

    plt.show()


def slope_field():
    for i in range(10):
        a = i * 2/9
        for j in range(10):
            b = j * 2/9
            get_line(a, b, 0.1)


def random_field():
    for i in range(2000):
        a = 2 * random.random()
        b = 2 * random.random()
        get_line(a, b, 0.1)


def get_line(t, y, length):
    s = 1 - 2 * t * y  # Slope
    c = length / 2     # Line Length
    a = t              # t Position
    b = y              # y Position

    db = math.sqrt((s**2*c**2)/(s**2+1))
    da = math.sqrt(c**2-db**2)

    plt.plot(a - da, b - db), (a + da, b + db)


if __name__ == "__main__":
    slope_field()
