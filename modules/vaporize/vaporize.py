import cv2
import numpy as np
from typ import Image as ImageType


CASCADE_FOLDER = 'res/cascade'

def vaporize(img: ImageType) -> ImageType:
    row, column, channel = img.shape
    mean = 0
    noise = 15
    sigma = noise ** 1
    gauss = np.random.normal(mean, sigma, (row, column, channel))
    gauss = gauss.reshape(row, column, channel)
    img = (img + gauss)
    cv2.normalize(img, img, 0, 1, cv2.NORM_MINMAX)

    return img
