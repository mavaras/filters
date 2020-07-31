import math
from typing import Tuple
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


def vangogh(
    img: ImageType,
    batch_size: int = 10000,
    blur_size: int = 3,
    min_stroke_length: int = 2,
    max_stroke_length: int = 8,
    angle: int = 90,
    stroke_scale_divider: int = 1000
) -> ImageType:
    grid = randomize_strokes_order(img)
    img_res = cv2.medianBlur(img, blur_size)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    palette = get_palette(img)
    fieldx, fieldy = apply_gaussian_blur(img_gray)

    for h in range(0, len(img), batch_size):
        for _, (y, x) in enumerate(grid[h : len(grid)]):
            color = palette[nearest_color(palette, img[y][x])]
            angle = math.degrees(math.atan2(fieldy[y, x], fieldx[y, x])) + angle
            stroke_scale = int(math.ceil(max(img.shape) / stroke_scale_divider))
            length = randint(min_stroke_length, max_stroke_length)
            cv2.ellipse(
                img_res,
                (x, y),
                (length, stroke_scale),
                angle, 0, 360, color, -1
            )

    return img_res
