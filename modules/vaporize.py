import random as rd
from typ import Image as ImageType

import cv2
import numpy as np


CASCADE_FOLDER = 'res/cascade'

def get_face_classifier() -> cv2.CascadeClassifier:
    return cv2.CascadeClassifier(
        f'{CASCADE_FOLDER}/haarcascade_frontalface_default.xml'
    )


def get_eyes_classifier() -> cv2.CascadeClassifier:
    return cv2.CascadeClassifier(f'{CASCADE_FOLDER}/haarcascade_eye.xml')


def vaporize(img: ImageType) -> ImageType:
    row, column, channel = img.shape
    mean = 0
    noise = 15
    sigma = noise ** 1
    gauss = np.random.normal(mean, sigma, (row, column, channel))
    gauss = gauss.reshape(row, column, channel)
    noisy = (img + gauss)
    cv2.normalize(noisy, noisy, 0, 1, cv2.NORM_MINMAX)

    return noisy
