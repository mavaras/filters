from typing import List
import random
import numpy as np
import cv2

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
    color_range: List[int],
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
                randomi(*color_range),
                channel
            )

    return img


def grayscale(img: ImageType, alpha: int, beta: int) -> ImageType:
    gray_mult = 0.07 * img[:, :, 2] + 0.72 * img[:, :, 1] + 0.21 * img[:, :, 0]
    gray_img = gray_mult.astype(np.uint8)
    gray_img = cv2.convertScaleAbs(gray_img, alpha=alpha, beta=beta)

    return gray_img + 0


def sepia(img: ImageType, mode: str = 'none') -> ImageType:
    for row in range(len(img)):
        for col in range(len(img[0])):
            img_r = img[row, col, 0]
            img_g = img[row, col, 1]
            img_b = img[row, col, 2]
            sepia_rgb = {
                'sepia_b': (img_r * 0.272 + img_g * 0.534 + img_b * 0.131),
                'sepia_g': (img_r * 0.349 + img_g * 0.686 + img_b * 0.168),
                'sepia_r': (img_r * 0.393 + img_g * 0.769 + img_b * 0.189)
            }
            if mode == 'randomize':
                rgb_channels = list(sepia_rgb.keys())
                random.shuffle(rgb_channels)
                sepia_rgb = {channel: sepia_rgb[channel] for channel in rgb_channels}
            elif mode == 'blue':
                aux = sepia_rgb['sepia_b']
                sepia_rgb['sepia_b'] = sepia_rgb['sepia_r']
                sepia_rgb['sepia_r'] = aux
            elif mode == 'green':
                aux = sepia_rgb['sepia_g']
                sepia_rgb['sepia_g'] = sepia_rgb['sepia_r']
                sepia_rgb['sepia_r'] = aux

            for itr, (_, value) in enumerate(sepia_rgb.items()):
                img[row, col, itr] = value if value <= 255 else 255

    return img
