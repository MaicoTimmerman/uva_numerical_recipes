# Vak: Numerical Recipes
# Auteurs: Robin Klusman 10675671, Maico Timmerman 10542590
try:
    import matplotlib.pyplot as plt
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


def show_images(images, cm=plt.cm.gray, axis='off'):
    """Shows an array of images in a figure-sublot

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


if __name__ == "__main__":
    pass
