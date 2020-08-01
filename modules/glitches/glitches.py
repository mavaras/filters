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
    draw_spilled_glitch
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
