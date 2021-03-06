import math
import random
import numpy as np
import cv2
from sklearn.cluster import KMeans

import matplotlib.pyplot as plt

from typ import (
    Image as ImageType,
    Palette as PaletteType
)


CASCADE_FOLDER = 'res/cascade'

def regulate(
    img: ImageType,
    hue: int = 0,
    saturation: int = 0,
    luminosity: int = 0
) -> ImageType:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV_FULL)
    if hue < 0:
        hue = 255 + hue
    hsv[:, :, 0] += hue
    clipped_addition(hsv[:, :, 1], saturation)
    clipped_addition(hsv[:, :, 2], luminosity)

    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR_FULL)


def clipped_addition(
    img: ImageType,
    x: int,
    maxn: int = 255,
    minn: int = 0
):
    if x > 0:
        mask = img > (maxn - x)
        img += x
        np.putmask(img, mask, maxn)
    if x < 0:
        mask = img < (minn - x)
        img += x
        np.putmask(img, mask, minn)


def nearest_color(palette: PaletteType, value: int) -> int:
    euclidean_distance = [np.linalg.norm(palette_color - value) for palette_color in palette]
    return euclidean_distance.index(min(euclidean_distance))


def direction(n_1: int, n_2: int) -> int:
    return math.atan2(n_1, n_2)


def randomi(low_lim: int, up_lim: int) -> int:
    return random.randint(low_lim, up_lim)


def randomized_grid(height: int, width: int, scale: int):
    grid = []
    rel = scale // 2
    for c in range(0, height, scale):
        for j in range(0, width, scale):
            y = random.randint(-rel, rel) + c
            x = random.randint(-rel, rel) + j
            grid.append((y % height, x % width))

    random.shuffle(grid)

    return grid


def randomize_strokes_order(img: ImageType):
    grid = []
    img_height, img_width, _ = img.shape
    for row in range(0, img_height, 2):
        for col in range(0, img_width, 2):
            grid.append((row, col))
    random.shuffle(grid)

    return grid


def get_palette(img: ImageType) -> PaletteType:
    clt = KMeans(n_clusters=24, n_jobs=1, n_init=10)
    clt.fit(img.reshape(-1, 3))
    palette = clt.cluster_centers_
    masks = [(0, 50, 0), (15, 30, 0), (-15, 30, 0), (-5, 220, 15)]
    extension = [
        regulate(
            palette.reshape((1, len(palette), 3)).astype(np.uint8),
            *mask
        ).reshape((-1, 3))
        for mask in masks
    ]

    return np.vstack([palette] + extension)


def show_palette(palette: PaletteType):
    cols = len(palette)
    rows = int(math.ceil(len(palette) / cols))
    palette_img = np.zeros((rows * 80, cols * 80, 3), dtype=np.uint8)
    for y in range(rows):
        for x in range(cols):
            if y * cols + x < len(palette):
                color = [int(c) for c in palette[y * cols + x]]
                cv2.rectangle(
                    palette_img,
                    (x * 80, y * 80),
                    (x * 80 + 80, y * 80 + 80),
                    color, -1
                )


def pixel_in_area(
    pixel_x: int,
    pixel_y: int,
    area_x: int,
    area_y: int,
    area_w: int,
    area_h: int
) -> bool:

    return (pixel_x >= area_x and pixel_x >= area_w) or (pixel_y >= area_y and pixel_y <= area_h)


def get_face_classifier() -> cv2.CascadeClassifier:
    return cv2.CascadeClassifier(
        f'{CASCADE_FOLDER}/haarcascade_frontalface_default.xml'
    )


def get_eyes_classifier() -> cv2.CascadeClassifier:
    return cv2.CascadeClassifier(f'{CASCADE_FOLDER}/haarcascade_eye.xml')


def get_faces(img: ImageType) -> np.ndarray:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = get_face_classifier()
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    return faces
