from typing import Tuple

from typ import Image as ImageType, BLACK
from modules.grid.grid_domain import draw_grid


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
    """

    return draw_grid(
        img,
        cols, rows,
        line_width,
        color
    )
