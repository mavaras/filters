from typing import List, Tuple

from modules.vangogh.vangogh_domain import draw_vangogh
from typ import Image as ImageType


# pylint: disable=too-many-locals, too-many-arguments, dangerous-default-value
def vangogh(
    img: ImageType,
    batch_size: int = 10000,
    blur_size: int = 3,
    stroke_length_range: List[int] = [2, 8],
    stroke_angle: int = 90,
    stroke_start_angle: int = 0,
    stroke_end_angle: int = 360,
    stroke_scale_divider: int = 1000
) -> ImageType:

    return draw_vangogh(*locals().values())
