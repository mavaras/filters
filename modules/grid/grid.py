from typing import Tuple

from typ import Image as ImageType, BLACK
from modules.grid.grid_domain import (
    draw_diagonal_grid,
    draw_grid
)


def grid(
    img: ImageType,
    cols: int,
    rows: int,
    line_width: int = 2,
    color: Tuple[int] = BLACK
) -> ImageType:
    """ Draws a grid of the specified size on the given image

    :param ImageType img: A numpy array representing an Image
    :param int cols: Number of columns of the grid
    :param int rows: Number of rows of the grid
    :param int line_width: Number of rows of the grid, defults to 2
    :param Tuple[int] color: Grid strokes color, defults to BLACK

    :return: Resultling image
    :rtype: ImageType

    .. image:: imgs/me.jpeg
        :scale: 65 %
    .. image:: imgs/me_grid.jpg
        :scale: 65 %
    """

    return draw_grid(
        img,
        cols, rows,
        line_width,
        color
    )


def diagonal_grid(
    img: ImageType,
    cols: int,
    rows: int,
    line_width: int = 2,
    color: Tuple[int] = BLACK,
    offset: int = 0
) -> ImageType:
    """ Draws a diagonal grid (45 degrees) of the specified size on the given image

    :param ImageType img: A numpy array representing an Image
    :param int cols: Number of columns of the grid
    :param int rows: Number of rows of the grid
    :param int line_width: Number of rows of the grid, defults to 2
    :param Tuple[int] color: Grid strokes color, defults to BLACK
    :param int offset: Grid strokes offset, defults to 0

    :return: Resultling image
    :rtype: ImageType
    """

    return draw_diagonal_grid(
        img,
        cols, rows,
        line_width,
        color,
        offset
    )
