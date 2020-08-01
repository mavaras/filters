from typing import Dict, List, Union
import numpy as np

from typ import (
    Image as ImageType,
    GlitchTypes
)
from utils import randomi


def draw_glitch(
    img: ImageType,
    area_x: int,
    area_y: int,
    area_w: int,
    area_h: int,
    n_slices: int,
    translation_x: Dict[str, int],
    gtype: str = 'normal'
) -> ImageType:
    _, img_width, _ = img.shape
    slice_heights = get_slice_height(area_h, n_slices, equals=True)
    prev_slice_height = 0

    for itr in range(0, n_slices):
        slice_height = slice_heights[itr]

        if gtype == GlitchTypes.ABSTRACT.value:
            inc = prev_slice_height
            glitch_end_y = area_y + sum(slice_heights[:itr]) + slice_height
        else:
            inc = itr * slice_height
            glitch_end_y = area_y + inc + slice_height
        glitch_start_y = area_y + inc

        dist = randomi(
            translation_x.get('low_lim', 0),
            translation_x.get('up_lim', 0)
        )

        glitch_w = area_x + dist
        if glitch_w + area_w > img_width:
            glitch_w -= (glitch_w + area_w - img_width)
        if gtype == GlitchTypes.CYCLE.value:
            glitch_w = area_x + area_w
            img[glitch_start_y:glitch_end_y, dist:area_x + glitch_w] = \
                img[glitch_start_y:glitch_end_y, :area_x + glitch_w - dist]
            img[glitch_start_y:glitch_end_y, area_x:dist] = \
                img[glitch_start_y:glitch_end_y, glitch_w - dist + area_x:glitch_w]
        else:
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
            index = randomi(0, 1)
            slice_height.append(int(heights[index]))

    return slice_height


def draw_offset_rect(
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


def draw_offset_rect_colorized(
    img,
    area_x: int,
    area_y: int,
    area_w: int,
    area_h: int,
    channel: int,
    randomize: bool = False
) -> ImageType:
    img_height, img_width, _ = img.shape
    offset_x = randomi(
       0,
        abs(img_width - (area_w + area_x))
    ) if randomize else 0
    offset_y = randomi(
        0,
        abs(img_height - (area_h + area_y))
    ) if randomize else 0
    img[
        area_y:area_y + area_h,
        area_x:area_x + area_w,
        channel
    ] = img[offset_y:area_h + offset_y, offset_x:area_w + offset_x, channel]

    return img


def draw_spilled_glitch(
    img: ImageType,
    area_x: int,
    area_y: int,
    area_w: int,
    area_h: int,
    start_pos: int,
    vertical: bool = False
) -> ImageType:
    if vertical:
        img = np.rot90(img[::-1])
    selection = (
        slice(start_pos, area_y + area_h),
        slice(area_x, area_x + area_w)
    )
    chunk = img[selection]

    for itr, pixel in enumerate(chunk[0]):
        sel = (selection[0], itr)
        img[sel] = pixel

    return np.rot90(img) if vertical else img
