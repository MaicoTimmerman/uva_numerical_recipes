# Vak: Numerical Recipes
# Auteurs: Robin Klusman 10675671, Maico Timmerman 10542590
try:
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy import ndimage, misc
    assert plt
    assert np
    assert ndimage, misc
except ImportError:
    print("""
          Warning: could not import matplotlib:pyplot,
          numpy or scipy:ndimage/misc
          """)

import filters


def convolve_image(img, filter_kernel):
    """ Convolves any given image with any given filter """
    return ndimage.convolve(img, filter_kernel, cval=0.0)


def show_images(images, cm=plt.cm.gray, axis='off', title=None):
    """
    Shows an array of images in a figure-sublot

    Args:
        img(list) - list of images

    Optional:
        cm(plt.cm) - maptlotlib colormap
        axis(str) - argument to give plt
    """
    number_images = len(images)
    fig = plt.figure(title)

    for i, img in enumerate(images):
        fig.add_subplot(1, number_images, i)
        plt.axis(axis)
        plt.imshow(img, cmap=cm)

    plt.show()


def prewitt_assignment(img):
    """
    Calculate the prewitt filtering of the img, then display vectors of the
    gradient on the img. Skip every third vector.
    """
    # Get filter:
    filter_x, filter_y = filters.prewitt()

    # Apply Filter
    Gx = convolve_image(img, filter_x)
    Gy = convolve_image(img, filter_y)

    # Create a grid to display gradient vectors
    len_x, len_y = np.shape(img)
    x, y = np.mgrid[:len_x, :len_y]

    # Calculate the prewitt image
    G = np.sqrt(Gx*Gx + Gy*Gy)

    # Display the x filtered gradient
    gradient = np.gradient(G)

    # Display the quiver on the image. Skip every first and second vector for
    # visibility purposes.
    skip = (slice(None, None, 3), slice(None, None, 3))
    plt.quiver(y[skip], x[skip],
               gradient[1][skip], gradient[0][skip],
               color='r', minlength=.2)

    # Show result
    plt.imshow(G, cmap=plt.cm.gray)
    plt.show()


def laplace_assignment(img):
    """
    Apply a laplacian filter on given img.
    """

    # Get filter
    filter = filters.laplace()

    # Apply filter
    filtered_img = convolve_image(img, filter)

    # Show results
    show_images([img, filtered_img], title="Laplacian")


def gauss_assignment(img):
    """
    Apply a laplacian filter on given img.
    """
    # Apply the gaussian filter.
    gauss_img = ndimage.gaussian_filter(img, 4)

    # Invert the gauss filter
    inverted_gaus_img = img - gauss_img

    # Show results
    show_images([inverted_gaus_img, img, gauss_img], title="Gaussian")


def sobel_assignment(img):
    """
    Apply a laplacian filter on given img.
    """
    # Get filter:
    filter_x, filter_y = filters.prewitt()

    # Apply Filter
    Sx = convolve_image(img, filter_x)
    Sy = convolve_image(img, filter_y)

    # Calculate the result image
    S = np.sqrt(Sx*Sx + Sy*Sy)

    # Show the results
    show_images([Sx, Sy, S], title="sobel")


if __name__ == "__main__":
    img = misc.lena()

    prewitt_assignment(img)
    gauss_assignment(img)
    laplace_assignment(img)
    sobel_assignment(img)
