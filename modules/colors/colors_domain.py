from typing import Dict, List

from typ import (
    Image as ImageType,
)
from utils import randomi


def colorize_image(
    img: ImageType,
    area_x: int,
    area_y: int,
    area_w: int,
    area_h: int,
    color: int,
    channel: int = slice(0, 2)
) -> ImageType:
    img[area_y:area_y + area_h, area_x:area_x + area_w, channel] = color

    return img


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
            img = colorize_image(
                img,
                area_x + col_inc,
                area_y + row_inc,
                col_width,
                row_height,
                randomi(color_range.get('low_lim'), color_range.get('up_lim')),
                channel
            )

    return img
