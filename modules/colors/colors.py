from typing import List
import modules.colors.colors_domain as colors_domain

from typ import Image as ImageType


def colorize(
  img: ImageType,
  area: List[int],
  color: int,
  channel: int = slice(0, 2)
) -> ImageType:
    """ Changes to given color the color channel of the given area for the given image

    :param ImageType img: A numpy array representing an image
    :param List[int] area: img area (x, y, w, h) to apply the filter
    :param int color: New color for given channel in area
    :param int channel: RGB channel

    :return: Resulting colorized image
    :rtype: ImageType

    .. image:: imgs/me.jpeg
        :scale: 65 %
    .. image:: imgs/me_colorize.jpg
        :scale: 65 %
    """

    return colors_domain.colorize_image(img, *area, color, channel)


def colorized_grid(
    img: ImageType,
    area: List[int],
    cols: int,
    rows: int,
    color_range: List[int],
    channel: int = slice(0, 2)
) -> ImageType:
    """ Changes to a random color between the given range the color channel of each
    square of the provided colsXrows grid.

    :param img ImageType: A numpy array representing an image
    :param List[int] area: img area (x, y, w, h) to apply the filter
    :param int cols: Number of columns of the desired grid
    :param int rows: Number of rows of the desired grid
    :param List[int] color_range: [min, max] range to obtain the random color for each grid square
    :param int channel: Color channel to modify. You can pass a range as an slice, defaults to slice[0:2] (all three RGB channels)

    :return: Resulting image
    :rtype: ImageType
    """

    return colors_domain.colorized_grid(
        img,
        *area,
        cols, rows,
        color_range,
        channel
    )


def grayscale(img: ImageType, alpha: int, beta: int) -> ImageType:
    """ Wraps opencv's convertScaleAbs() function for generating a grayscale image
    of the given one.

    :param ImageType img: A numpy array representing an image
    :param int alpha: opencv's convertScaleAbs alpha parameter
    :param int beta: opencv's convertScaleAbs beta parameter

    :return: Resulting grayscaled image
    :rtype: ImageType
    """

    return colors_domain.grayscale(img, alpha, beta)


def sepia(img: ImageType, mode: str = 'none') -> ImageType:
    """ Applies classic sepia filter to the given image.

    :param ImageType img: A numpy array representing an image
    :param str mode: 'none', 'randomize', 'blue', 'green', defults to 'none'

    :return: Resulting image
    :rtype: ImageType
    """

    return colors_domain.sepia(img, mode)


def negative(img: ImageType) -> ImageType:
    """ Wraps numpy's vecorize so image gets inverted

    :param ImageType img: A numpy array representing an image

    :return: Resulting image
    :rtype: ImageType

    .. image:: imgs/me.jpeg
        :scale: 65 %
    .. image:: imgs/me_negative.jpg
        :scale: 65 %
    """

    return colors_domain.negative(img)
