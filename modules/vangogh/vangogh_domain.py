import math
from typing import List, Tuple
from random import randint

from typ import Image as ImageType
import cv2
from utils import (
    get_palette,
    nearest_color,
    randomize_strokes_order
)


def apply_gaussian_blur(img: ImageType) -> Tuple[ImageType, ImageType]:
    kernel_size = 2 * int(round(max(img.shape) / 50)) + 1
    kernel = (kernel_size, kernel_size)
    fieldx = cv2.Scharr(img, cv2.CV_32F, 1, 0) / 15.36
    fieldy = cv2.Scharr(img, cv2.CV_32F, 0, 1) / 15.36

    for _ in range(1):
        fieldx = cv2.GaussianBlur(fieldx, kernel, 0)
        fieldy = cv2.GaussianBlur(fieldy, kernel, 0)

    return fieldx, fieldy


# pylint: disable=too-many-locals, too-many-arguments, dangerous-default-value
def draw_vangogh(
    img: ImageType,
    area_x: int,
    area_y: int,
    area_w: int,
    area_h: int,
    batch_size,
    blur_size,
    stroke_length_range,
    stroke_angle,
    stroke_start_angle,
    stroke_end_angle,
    stroke_scale_divider
) -> ImageType:
    area = img[area_y:area_y + area_h, area_x:area_x + area_w]
    grid = randomize_strokes_order(area)
    img_res = cv2.medianBlur(img, blur_size)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    palette = get_palette(area)
    fieldx, fieldy = apply_gaussian_blur(img_gray)

    for height in range(0, len(img), batch_size):
        for _, (y, x) in enumerate(grid[height:len(grid)]):
            color = palette[nearest_color(palette, img[y + area_y][x + area_x])]
            rotation_angle = math.degrees(math.atan2(fieldy[y, x], fieldx[y, x])) + stroke_angle
            stroke_scale = int(math.ceil(max(img.shape) / stroke_scale_divider))
            length = randint(*stroke_length_range)
            cv2.ellipse(
                img_res,
                (x + area_x, y + area_y),
                (length, stroke_scale),
                rotation_angle,
                stroke_start_angle, stroke_end_angle,
                color, -1
            )

    return img_res
