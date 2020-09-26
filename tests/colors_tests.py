#! /usr/bin/env python

import os
import uuid
import cv2
from modules import colors


if not os.path.isdir('tests/tmp'):
    os.mkdir('tests/tmp')

TEST_IMG = 'imgs/me.jpeg'

def assert_images(img_1, img_2):
    return (img_1 == img_2).all()


def save_tmp_image(img):
    filename = f'tests/tmp/timg_{uuid.uuid4()}.jpg'
    cv2.imwrite(filename, img)
    return filename


def test_negative():
    img = colors.negative(cv2.imread(TEST_IMG))
    res = cv2.imread(save_tmp_image(img))
    assert assert_images(res, cv2.imread('_docs/imgs/me_negative.jpg'))

def test_grayscale():
    img = colors.grayscale(cv2.imread(TEST_IMG), 1, 1)
    res = cv2.imread(save_tmp_image(img))
    assert assert_images(res, cv2.imread('_docs/imgs/me_grayscale.jpg'))

def test_sepia():
    img_sepia = colors.sepia(cv2.imread(TEST_IMG))
    res = cv2.imread(save_tmp_image(img_sepia))
    assert assert_images(res, cv2.imread('_docs/imgs/me_sepia.jpg'))

def test_colorize():
    img = colors.colorize(cv2.imread(TEST_IMG), area=[10, 10, 500, 250], color=125)
    res = cv2.imread(save_tmp_image(img))
    assert assert_images(res, cv2.imread('_docs/imgs/me_colorize.jpg'))
