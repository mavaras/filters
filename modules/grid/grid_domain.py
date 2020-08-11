from typing import Tuple

from typ import Image as ImageType


def draw_grid(
    img: ImageType,
    cols: int,
    rows: int,
    line_width: int,
    color: Tuple[int]
) -> ImageType:
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
