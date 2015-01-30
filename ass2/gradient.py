# Vak: Numerical Recipes
# Auteurs: <Naam> <Collegakaart>, <Naam> <Collekaart>
try:
    import matplotlib.pyplot as plt
except ImportError:
    print "Warning: could not import matplotlib.pyplot"
try:
    import numpy as np
    assert np
except ImportError:
    print "Warning: could not import numpy"
try:
    from scipy import ndimage, misc
    assert ndimage, misc
except ImportError:
    print "Warning: could not import scipy.ndimage"

import filters


def convolve_image(img, filter_kernel):
    """Convolves any given image with any given filter"""
    return ndimage.convolve(img, filter_kernel, cval=0.0)


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


def prewitt_assignment(img):
    """"""
    # Get filter:
    filter_x, filter_y = filters.prewitt()
    x, y = np.shape(img)

    # Apply Filter
    gradient_x = convolve_image(img, filter_x)[::-1]
    gradient_y = convolve_image(img, filter_y)[::-1]

    # quiver ....

    # Show result
    show_images([img, gradient_x, gradient_y])


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
    img = ndimage.imread('img/gauss.png')

    prewitt_assignment(img)

    # call other sub-assignments
