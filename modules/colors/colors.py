from typing import List
import modules.colors.colors_domain as colors_domain

from typ import Image as ImageType


def colorize(
  img: ImageType,
  area: List[int],
  color: int,
  channel: int = slice(0, 2)
) -> ImageType:

    return colors_domain.colorize_image(img, *area, color, channel)


def colorized_grid(
    img: ImageType,
    area: List[int],
    cols: int,
    rows: int,
    color_range: List[int],
    channel: int = slice(0, 2)
) -> ImageType:

    return colors_domain.colorized_grid(
        img,
        *area,
        cols, rows,
        color_range,
        channel
    )


def grayscale(img: ImageType, alpha: int, beta: int) -> ImageType:

    return colors_domain.grayscale(img, alpha, beta)


def sepia(img: ImageType, mode: str = 'none') -> ImageType:

    return colors_domain.sepia(img, mode)
