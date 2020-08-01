from typing import Dict, List, Union
import random
import cv2

from typ import Image as ImageType, BLACK
from modules.vaporize import get_face_classifier


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


def cycle_glitch(
    img: ImageType,
    translation_x: Dict[str, int],    

    area_x: int,
    area_y: int,
    area_w: int,
    area_h: int,

    n_slices: int = 20
) -> ImageType:
    slice_height = round(area_h / n_slices)

    for itr in range(0, n_slices):
        inc = itr * slice_height
        glitch_start_y = area_y + inc
        glitch_end_y = area_y + inc + slice_height
        offset = random.randint(
            translation_x.get('low_lim', 0),
            translation_x.get('up_lim', 0)
        )
        glitch_w = area_x + area_w
        img[glitch_start_y:glitch_end_y, offset:area_x + glitch_w] = \
            img[glitch_start_y:glitch_end_y, :area_x + glitch_w - offset]
        img[glitch_start_y:glitch_end_y, area_x:offset] = \
            img[glitch_start_y:glitch_end_y, glitch_w - offset:glitch_w]

    return img


def draw_glitch(
    img: ImageType,
    area_x: int,
    area_y: int,
    area_w: int,
    area_h: int,
    n_slices: int,
    translation_x: Dict[str, int],
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
        glitch_end_y = area_y + inc + slice_height
        dist = random.randint(
            translation_x.get('low_lim', 0),
            translation_x.get('up_lim', 0)
        )

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


def offset_rectangle(
    img,
    start_x: int,
    start_y: int,
    chunk_length: int,
    side: str
) -> ImageType:
    img_height, img_width, _ = img.shape
    chunk_length = min(chunk_length, img_height - start_y)
    stop_y = start_y + chunk_length

    if side == 'left':
        stop_x = img_width - start_x
        chunk = img[start_y:stop_y, start_x:]
        img[start_y:stop_y, :stop_x] = chunk
    else:
        stop_x = start_x
        chunk = img[start_y:stop_y, :img_width - start_x]
        img[start_y:stop_y, stop_x:] = chunk

    return img


def offset_rect_colorized(
    img: ImageType,
    area: List[int],
    channel: int = 1,
    randomize: bool = False
 ) -> ImageType:

    return draw_offset_rect_colorized(img, *area, channel, randomize)


def draw_offset_rect_colorized(
    img,
    area_x: int = 50,
    area_y: int = 50,
    area_w: int = 120,
    area_h: int = 410,
    channel: int = 1,
    randomize: bool = False
) -> ImageType:
    img_height, img_width, _ = img.shape
    offset_x = random.randint(
       0,
        abs(img_width - (area_w + area_x))
    ) if randomize else 0
    offset_y = random.randint(
        0,
        abs(img_height - (area_h + area_y))
    ) if randomize else 0
    img[
        area_y:area_y + area_h,
        area_x:area_x + area_w,
        channel
    ] = img[offset_y:area_h + offset_y, offset_x:area_w + offset_x, channel]

    return img
