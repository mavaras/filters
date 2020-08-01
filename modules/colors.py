from typing import Dict

from typ import (
    Image as ImageType,
)
from utils import randomi


def colorized_grid(
    img: ImageType,
    area_x: int,
    area_y: int,
    area_w: int,
    area_h: int,
    cols: int,
    rows: int,
    color_range: Dict[str, int],
    channel: int
) -> ImageType:
    row_height = round(area_h / rows)
    col_width = round(area_w / cols)
    for row in range(rows):
        row_inc = row * row_height
        for col in range(cols):
            col_inc = col * col_width
            img[
                area_y + row_inc:area_y + row_inc + row_height,
                area_x + col_inc:area_x + col_inc + col_width,
                channel
            ] = randomi(color_range.get('low_lim'), color_range.get('up_lim'))

    return img
