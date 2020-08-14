import cv2
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


def draw_diagonal_grid(
    img: ImageType,
    cols: int,
    rows: int,
    line_width: int,
    color: Tuple[int]
) -> ImageType:
    img_height, img_width, _ = img.shape
    row_height = img_height // rows
    col_width = img_width // cols
    start_poss = []
    end_poss = []
    for row in range(rows):
        row_pos = row_height * row
        start_poss += [(0, row_pos), (row_pos, 0)]
        end_poss += [(img_height - row_pos, img_width), (img_height, img_width - row_pos)]
    for col in range(cols):
        col_pos = col_width * col
        start_poss += [(img_width, col_pos), (0, img_height - col_pos)]
        end_poss += [(col_pos, img_height), (img_width - col_pos, 0)]

    for itr in range(len(start_poss)):
        img = cv2.line(
            img,
            start_poss[itr],
            end_poss[itr],
            color,
            line_width
        )

    return img
