from typing import List

from modules.vangogh.vangogh_domain import draw_vangogh
from typ import Image as ImageType
from utils import get_faces


# pylint: disable=unused-argument, too-many-locals, too-many-arguments, dangerous-default-value
def vangogh(
    img: ImageType,
    area: List[int] = None,
    pattern_image: ImageType = None,
    face: bool = False,
    batch_size: int = 10000,
    blur_size: int = 3,
    stroke_length_range: List[int] = [2, 8],
    stroke_angle: int = 90,
    stroke_start_angle: int = 0,
    stroke_end_angle: int = 360,
    stroke_scale_divider: int = 1000
) -> ImageType:
    """ Applies the vangogh filter to given image. This filter is about simulating kind
    of brush strokes based on image color palette with different configuration parameters.

    :param ImageType img: A numpy array representing an Image
    :param List[int] area: img area (x, y, w, h) to apply the filter, defaults to None
    :param ImageType pattern_image:
        another image which will act as a color template,
        so palette colors will be taken from this image instead of from img, defaults to None
    :param bool face: If True filter is applied to img face area (if exists), defaults to False
    :param int batch_size: not so useful, defaults to 10000
    :param int blur_size: Gaussian Blur kernel size, defaults to 3
    :param List[int] stroke_length_range: [min, max] range for strokes length, defaults to [2, 8]
    :param int stroke_angle: Whole strokes rotation angle, defaults to 90
    :param int stroke_start_angle: Strokes start angle, defaults to 0
    :param int stroke_end_angle: Strokes end angle, defaults to 360
    :param int stroke_scale_divider: [description], defaults to 1000

    :return ImageType: Resulting image
    :rtype: ImageType

    .. image:: imgs/me.jpeg
        :scale: 65 %
    .. image:: imgs/me_vangogh.jpg
        :scale: 65 %
    .. image:: imgs/me_vangogh2.jpg
        :scale: 65 %
    .. image:: imgs/me_vangogh3.jpg
        :scale: 65 %
    .. image:: imgs/me_vangogh5.jpg
        :scale: 65 %
    .. image:: imgs/me_vangogh4.jpg
        :scale: 65 %
    """

    if face:
        faces = get_faces(img)
        area = [int(element) for element in faces[0]]
        del face, faces
    elif not area:
        area = [0, 0, img.shape[1], img.shape[0]]
        del face

    return draw_vangogh(img, *area, *list(locals().values())[2:])
