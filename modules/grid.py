from typing import Tuple

from typ import Image as ImageType, BLACK


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

    img_height, img_width, _ = img.shape
    row_height = img_height // rows
    col_width = img_width // cols
    for row in range(rows):
        row_pos = row_height * row
        img[row_pos:row_pos + line_width, :] = color
    for col in range(cols):
        col_pos = col_width * col
        img[:, col_pos:col_pos + line_width] = color

    return img
