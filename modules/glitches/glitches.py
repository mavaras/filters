from typing import Dict, List, Tuple
import cv2
import numpy as np

from typ import (
    Image as ImageType,
)
from modules.glitches.glitches_domain import (
    draw_glitch,
    draw_offset_rect,
    draw_offset_rect_colorized,
    draw_pixelize_glitch,
    draw_spilled_glitch,
    draw_pixelize_glitch_vanish,
    multiply_image,
    draw_glitch_bytes,
    draw_glitch_sharp
)
from utils import get_faces


def glitch_bytes(
    img: str,
    intensity: float = 0.1
) -> ImageType:
    """ This is the classic random glitch filter for an image. It depends on the provided
    image extension and returns a 'random' result of glitching & deforming the image.
    So my suggestion is to test it multiple times with the same image to see the different
    kinds of possible results.
    For now, it works with .jpg, .jpeg, .png, .bmp, .gif and .tiff.
    I recommend you to highly reduce the intensity for large images.

    :param str img: The filepath of the image
    :param float intensity: Image deformation intensity, defaults to 0.1

    :return: Glitched image
    :rtype: ImageType

    .. image:: imgs/me.jpeg
        :scale: 65 %
    .. image:: imgs/me_glitch_bytes1.jpg
        :scale: 65 %
    .. image:: imgs/me_glitch_bytes2.jpg
        :scale: 65 %
    .. image:: imgs/me_glitch_bytes3.jpg
        :scale: 65 %
    """

    with open(img, 'rb') as imgb:
        header_size = {
            'jpg': 9,
            'jpeg': 9,
            'png': 8,
            'bmp': 54,
            'gif': 14,
            'tiff': 8
        }
        return draw_glitch_bytes(
            imgb,
            header_size.get(img.split('.')[-1]),
            intensity
        )


# pylint: disable=dangerous-default-value
def glitch(
    img: ImageType,
    area: List[int] = None,
    translation_x: List[int] = [0, 0],
    face: bool = False,
    n_slices: int = 20
) -> ImageType:
    """ Draws kind of 'artificial' glitch effect on the specified area of the provided
    image, by drawing different distortioned 'slices'.

    :param ImageType img: A numpy array representing an image
    :param List[int] translation_x: [min, max] range for generating random glitch slices width
    :param List[int] area: img area (x, y, w, h) to apply the filter, default to None (all image)
    :param bool face: If True filter is applied to img face area (if exists), defaults to False
    :param int n_slices: nº of glitch 'slices' that will appear in the provided area, defaults to 20

    :return: Resulting image
    :rtype: ImageType
    """

    if face:
        faces = get_faces(img)
        for _face in faces:
            _face = [int(element) for element in _face]
            draw_glitch(img, *_face, n_slices, translation_x)
    else:
        draw_glitch(img, *area, n_slices, translation_x)

    return img


# pylint: disable=dangerous-default-value
def abstract_glitch(
    img: ImageType,
    area: List[int] = None,
    translation_x: List[int] = [0, 0],
    n_slices: int = 20
) -> ImageType:
    """ Applies a glitch based on a pattern of repetition of rectangles in the specified area
     of the given image.

    :param ImageType img: A numpy array representing an image
    :param List[int] translation_x: [min, max] range for generating random glitch rectangles width
    :param List[int] area: img area (x, y, w, h) to apply the filter, default to None (all image)
    :param int n_slices: nº of glitch 'slices' that will appear in the provided area, defaults to 20

    :return: Resulting image
    :rtype: ImageType

    .. image:: imgs/me.jpeg
        :scale: 65 %
    .. image:: imgs/me_abstract_glitch1.jpg
        :scale: 65 %
    .. image:: imgs/me_abstract_glitch2.jpg
        :scale: 65 %
    .. image:: imgs/me_abstract_glitch3.jpg
        :scale: 65 %
    """

    draw_glitch(
        img,
        *area,
        n_slices=n_slices,
        translation_x=translation_x,
        gtype='abstract'
    )

    return img


# pylint: disable=dangerous-default-value
def cycle_glitch(
    img: ImageType,
    area: List[int],
    translation_x: List[int],
    n_slices: int = 20
) -> ImageType:
    """  Draws kind of 'artificial' glitch effect on the specified area of the provided
    image, by drawing different distortioned 'slices'. This is like the :func:`glitch` but
    making the slices follow a cyclic distortion.

    :param ImageType img: A numpy array representing an image
    :param List[int] translation_x: [min, max] range for generating random glitch slices width
    :param List[int] area: img area (x, y, w, h) to apply the filter, default to None (all image)
    :param int n_slices:
        nº of glitch 'slices' that will appear in the provided area, defaults to 20

    :return: Resulting image
    :rtype: ImageType

    .. image:: imgs/me.jpeg
        :scale: 65 %
    .. image:: imgs/me_cycle_glitch.jpg
        :scale: 65 %
    """

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
    """  Select a rectangle with the provided data whithin the image and translates it left
    or right as desired.

    :param ImageType img: A numpy array representing an image
    :param int start_x: x start position for the rectangle
    :param int start_y: y start position for the rectangle
    :param int chunk_length: rectangle width
    :param int side: 'left' or 'right' for the rectangle's position

    :return: Resulting image
    :rtype: ImageType

    .. image:: imgs/me.jpeg
        :scale: 65 %
    .. image:: imgs/me_offset_rect.jpg
        :scale: 65 %
    """

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
    """ Takes the desired area of the provided image and makes a 'colorized translation' of it
    based on the provided color channel of the (0,0, area_w,area_h) selection of the image.

    :param ImageType img: A numpy array representing an image
    :param List[int] area: img area (x, y, w, h) to apply the filter, default to None (all image)
    :param int channel: Color channel to modify. You can pass a range as an slice, defaults to 1
    :param bool randomize: If True, randomized the area offset, defaults to False

    :return: Resulting image
    :rtype: ImageType

    .. image:: imgs/me.jpeg
        :scale: 65 %
    .. image:: imgs/me_offset_rect_colorized.jpg
        :scale: 65 %
    """

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
    """ Spills down or right the area up/left header pixel colors creating
    a cascade of colorized lines.

    :param ImageType img: A numpy array representing an image
    :param List[int] area: img area (x, y, w, h) to apply the filter, default to None (all image)
    :param int start_pos: y/x point where to start spilling from, depending on vertical parameter
    :param bool vertical:
        If True, spilled is applied based on an x start pos,
        else is based on the y start_pos, defaults to False

    :return: Resulting image
    :rtype: ImageType

    .. image:: imgs/me.jpeg
        :scale: 65 %
    .. image:: imgs/me_spilled.jpg
        :scale: 65 %
    """

    return draw_spilled_glitch(
        img,
        *area,
        start_pos,
        vertical
    )


# pylint: disable=dangerous-default-value, too-many-arguments
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
    """ Draws a pattern of colorized pixel or slice over the area of the provided image.
    It can be with random colors or based on image palette.

    :param ImageType img: A numpy array representing an image
    :param List[int] area: img area (x, y, w, h) to apply the filter, default to None (all image)
    :param int n_slices: nº of glitch 'rows' that will appear in the provided area
    :param str gtype: 'image_based', 'image_based_inv', 'image_based_rand' or 'random', defaults to 'random'
    :param bool by_pixel:
        If true, the colorize process will be applied to each pixel,
        if False it will be applied to slices of a determined width, defaults to True
    :param int channel: Color channel to modify. You can pass a range as an slice, defaults to None
    :param List[int] random_slice_width_range:
        min/max of the range for randomly choose each slice width, defaults to [90, 220]
    :param List[int] random_color_range:
        min/max of the range in which random colors will be generated, defaults to [15, 260]
    :param List[int] skip_slices_range:
        min/max of a range for randomly exclude some rows of this effect, defaults to None

    :return: Resulting image
    :rtype: ImageType

    .. image:: imgs/me.jpeg
        :scale: 65 %
    .. image:: imgs/me_pixelize3.jpg
        :scale: 65 %
    .. image:: imgs/me_pixelize4.jpg
        :scale: 65 %
    .. image:: imgs/me_pixelize5.jpg
        :scale: 65 %
    .. image:: imgs/me_pixelize2.jpg
        :scale: 65 %
    .. image:: imgs/me_pixelize1.jpg
        :scale: 65 %
    """

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
    """ This is a particular glitch that applies a kind of 'vanish' effect to image content based on
    the sampling factor provided. The result depends of the sampling factor which sould be based on
    the image size.

    :param ImageType img: A numpy array representing an image
    :param int sampling_factor:
        Represents the intensity of the 'vanish' applied to the image. As greater, more distorsion
        more 'pixelized' the image will look like

    :return: Resulting image
    :rtype: ImageType

    .. image:: imgs/me.jpeg
        :scale: 65 %
    .. image:: imgs/me_vanish.jpg
        :scale: 65 %
    """

    return draw_pixelize_glitch_vanish(img, sampling_factor)


def glitch_sharp(img: ImageType, kernel: Tuple[int, int] = (3, 3)) -> ImageType:
    return draw_glitch_sharp(img, kernel)


def multiply(img: ImageType, factor: int) -> ImageType:
    """ not documented yet
    """

    return multiply_image(img, factor)
