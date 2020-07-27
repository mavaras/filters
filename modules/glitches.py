from typing import List
import cv2
import random

from .vaporize import get_face_classifier
from typ import Image as ImageType


def glitch(
    img: ImageType,
    area: List[int] = None,
    face: bool = False
) -> ImageType:
    if face:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_cascade = get_face_classifier()
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for face in faces:
            face = [int(element) for element in face]
            draw_glitch(img, *face)
    else:
        draw_glitch(img, *area)

    return img


def draw_glitch(
    img: ImageType,
    area_x: int,
    area_y: int,
    area_w: int,
    area_h: int
) -> ImageType:
    n_glitches = 20
    glitch_height = round(area_h / n_glitches)
    for itr in range(0, n_glitches):
        glitch_start_y = area_y + (itr * glitch_height)
        glitch_end_y = area_y + (itr * glitch_height + glitch_height)
        dist = random.randint(15, area_w // 2)
        img[glitch_start_y:glitch_end_y, (area_x + dist):area_x + area_w + dist] = \
            img[glitch_start_y:glitch_end_y, area_x:area_x + area_w]

    return img
