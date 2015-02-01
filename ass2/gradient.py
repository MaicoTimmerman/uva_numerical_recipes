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

import filters


def convolve_image(img, filter_kernel):
    """ Convolves any given image with any given filter """
    return ndimage.convolve(img, filter_kernel, cval=0.0)


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


def prewitt_assignment(img):
    """

    """
    # Get filter:
    filter_x, filter_y = filters.prewitt()

    x, y = np.shape(img)

    # Apply Filter
    filtered_x = convolve_image(img, filter_x)
    # filtered_y = convolve_image(img, filter_y)

    # Create a grid to display gradient vectors
    grid_x, grid_y = np.mgrid[0:x, 0:y]
    skip = (slice(None, None, 5), slice(None, None, 5))

    # Display the x filtered gradient
    dx, dy = np.gradient(filtered_x)
    plt.quiver(grid_y[skip], grid_x[skip], dy[skip], dx[skip])

    plt.imshow(img, cmap=plt.cm.gray)

    plt.show()

    # Show result

    # show_images([filtered_x, filtered_y])


def laplace_assignment(img):
    """"""
    pass


def gauss_assignment(img):
    """"""
    pass


def sobel_assignment(img):
    """"""
    pass


if __name__ == "__main__":
    # START HERE
    # img = misc.lena()
    img = ndimage.imread('img/lena.png', flatten=True)

    prewitt_assignment(img)

    # call other sub-assignments
