import cv2
import numpy as np

from typ import Image as ImageType


def draw_vaporize(
    img: ImageType,
    mean: int,
    noise: int
) -> ImageType:
    img_height, img_width, color_channel = img.shape
    sigma = noise ** 1
    gauss = np.random.normal(
        mean,
        sigma,
        (img_height, img_width, color_channel)
    )
    gauss = gauss.reshape(img_height, img_width, color_channel)
    img = (img + gauss)
    cv2.normalize(img, img, 0, 1, cv2.NORM_MINMAX)

    return img
