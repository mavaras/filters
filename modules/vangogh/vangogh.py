from typing import List, Tuple
import cv2

from modules.vangogh.vangogh_domain import draw_vangogh
from modules.vaporize import get_face_classifier
from typ import Image as ImageType


# pylint: disable=too-many-locals, too-many-arguments, dangerous-default-value
def vangogh(
    img: ImageType,
    area: List[int] = None,
    face: bool = False,
    batch_size: int = 10000,
    blur_size: int = 3,
    stroke_length_range: List[int] = [2, 8],
    stroke_angle: int = 90,
    stroke_start_angle: int = 0,
    stroke_end_angle: int = 360,
    stroke_scale_divider: int = 1000
) -> ImageType:
    if face:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_cascade = get_face_classifier()
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        area = [int(element) for element in faces[0]]
        del face, gray, face_cascade, faces
    elif not area:
        area = [0, 0, img.shape[1], img.shape[0]]

    return draw_vangogh(img, *area, *list(locals().values())[2:])
