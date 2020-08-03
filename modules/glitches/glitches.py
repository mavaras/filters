from typing import Dict, List
import cv2
import numpy as np

from typ import (
    Image as ImageType,
)
from modules.vaporize import get_face_classifier
from modules.glitches.glitches_domain import (
    draw_glitch,
    draw_offset_rect,
    draw_offset_rect_colorized,
    draw_pixelize_glitch,
    draw_spilled_glitch,
    draw_pixelize_glitch_vanish,
    multiply_image
)


def glitch(
    img: ImageType,
    translation_x: Dict[str, int],
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
            draw_glitch(img, *_face, n_slices, translation_x)
    else:
        draw_glitch(img, *area, n_slices, translation_x)

    return img


def abstract_glitch(
    img: ImageType,
    translation_x: Dict[str, int],
    area: List[int] = None,
    n_slices: int = 20
) -> ImageType:
    draw_glitch(
        img,
        *area,
        n_slices=n_slices,
        translation_x=translation_x,
        gtype='abstract'
    )

    return img


def cycle_glitch(
    img: ImageType,
    translation_x: Dict[str, int],
    area: List[int],
    n_slices: int = 20
) -> ImageType:
    draw_glitch(
        img,
        *area,
        n_slices=n_slices,
        translation_x=translation_x,
        gtype='cycle'
    )

    return img


def offset_rect(
    img,
    start_x: int,
    start_y: int,
    chunk_length: int,
    side: str
) -> ImageType:

    return draw_offset_rect(
        img,
        start_x, start_y,
        chunk_length,
        side
    )


def offset_rect_colorized(
    img: ImageType,
    area: List[int],
    channel: int = 1,
    randomize: bool = False
 ) -> ImageType:

    return draw_offset_rect_colorized(
        img,
        *area,
        channel,
        randomize
    )


def spilled_glitch(
    img: ImageType,
    area: List[int],
    start_pos: int,
    vertical: bool = False
) -> ImageType:

    return draw_spilled_glitch(
        img,
        *area,
        start_pos,
        vertical
    )


# pylint: disable=dangerous-default-value
def pixelize_glitch(
    img: ImageType,
    area: List[int],
    n_slices: int,
    gtype: str = 'random',
    by_pixel: bool = True,
    channel: int = None,
    random_slice_width_range: List[int] = [90, 220],
    random_color_range: List[int] = [15, 260],
    skip_slices_range: List[int] = None
) -> ImageType:

    return draw_pixelize_glitch(
        img,
        *area,
        n_slices,
        gtype,
        by_pixel,
        channel,
        random_slice_width_range,
        random_color_range,
        skip_slices_range
    )


def pixelize_glitch_vanish(
    img: ImageType,
    sampling_factor: int
) -> ImageType:

    return draw_pixelize_glitch_vanish(img, sampling_factor)


def multiply(img: ImageType, factor: int) -> ImageType:

    return multiply_image(img, factor)
