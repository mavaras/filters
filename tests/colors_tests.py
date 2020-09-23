#! /usr/bin/env python

import os
import uuid
import cv2
from modules import colors


if not os.path.isdir('tests/tmp'):
    os.mkdir('tests/tmp')

TEST_IMG = cv2.imread('imgs/me.jpeg')

def assert_images(img_1, img_2):
    return (img_1 == img_2).all()


def save_tmp_image(img):
    filename = f'tests/tmp/timg_{uuid.uuid4()}.jpg'
    cv2.imwrite(filename, img)
    return filename


def test_negative():
    img = colors.negative(TEST_IMG)
    res = cv2.imread(save_tmp_image(img))
    assert assert_images(res, cv2.imread('_docs/imgs/me_negative.jpg'))

def test_grayscale():
    img = colors.grayscale(TEST_IMG, 1, 1)
    res = cv2.imread(save_tmp_image(img))
    assert assert_images(res, cv2.imread('_docs/imgs/me_grayscale.jpg'))

def test_sepia():
    img = colors.sepia(TEST_IMG)
    res = cv2.imread(save_tmp_image(img))
    assert assert_images(res, cv2.imread('_docs/imgs/me_sepia.jpg'))
