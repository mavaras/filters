from typing import List, Union
import random
import cv2

from typ import Image as ImageType
from modules.vaporize import get_face_classifier


def glitch(
    img: ImageType,
    area: List[int] = None,
    face: bool = False,
    n_slices: int = 20
) -> ImageType:
    if face:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_cascade = get_face_classifier()
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for _face in faces:
            _face = [int(element) for element in _face]
            draw_glitch(img, *_face, n_slices)
    else:
        draw_glitch(img, *area, n_slices)

    return img


def abstract_glitch(
    img: ImageType,
    area: List[int] = None,
    n_slices: int = 20
) -> ImageType:
    draw_glitch(
        img,
        *area,
        n_slices=n_slices,
        abstract=True
    )
    return img


def draw_glitch(
    img: ImageType,
    area_x: int,
    area_y: int,
    area_w: int,
    area_h: int,
    n_slices: int,
    abstract: bool = False
) -> ImageType:
    _, img_width, _ = img.shape
    slice_heights = get_slice_height(area_h, n_slices, equals=True)
    prev_slice_height = 0

    for itr in range(0, n_slices):
        slice_height = slice_heights[itr]
        if not abstract:
            inc = itr * slice_height
        else:
            inc = prev_slice_height
        glitch_start_y = area_y + inc
        glitch_end_y = area_y + (sum(slice_heights[:itr]) + slice_height)
        dist = random.randint(15, 30)

        glitch_w = area_x + dist
        if glitch_w + area_w > img_width:
            glitch_w -= (glitch_w + area_w - img_width)
        img[glitch_start_y:glitch_end_y, glitch_w:glitch_w + area_w] = \
            img[glitch_start_y:glitch_end_y, area_x:area_x + area_w]

        prev_slice_height = slice_height

    return img


def get_slice_height(
    area_h: int,
    n_slices: int = None,
    equals: bool = True
) -> Union[int, List[int]]:
    eq_height = round(area_h / n_slices)
    if equals:
        slice_height = [eq_height for _ in range(n_slices)]
    else:
        slice_height = []
        heights = [area_h // (n_slices - 2), area_h // (n_slices + 2)]
        for _ in range(n_slices):
            index = random.randint(0, 1)
            slice_height.append(int(heights[index]))

    return slice_height
