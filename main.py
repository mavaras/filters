import sys
import time
import random
import argparse
import uuid
import cv2
from typ import Palette
from modules import (
    vangogh,
    vaporize,
    glitches
)


PARSER = argparse.ArgumentParser('filters cli')
PARSER.add_argument('-i', '--image')
PARSER.add_argument('-wo', '--write_output', action='store_true')
ARGS = PARSER.parse_args()


IMG_PATH = ARGS.image or 'imgs/me.jpeg'

def main():
    img = cv2.imread(IMG_PATH)
    # grid = randomize_strokes_order(img)
    h, w, _ = img.shape
    print(f'Image dimensions. {h}x{w}')
    area = {
        'x': w // 3,
        'y': 10,
        'width': int(w // 1.8),
        'height': 320,
    }
    '''img_ress = glitches.offset_rect_colorized(
        img,
        area.values(),
        channel=2,
        randomize=True
    )'''
    img_res = glitches.test(img, 200, 0, 600)
    if ARGS.write_output:
        cv2.imwrite(f'outimgs/out_{uuid.uuid4()}.jpg', img_res)
    cv2.imshow('img_res', img_res)
    cv2.waitKey(0)


if __name__ == '__main__':
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f'execution time: {elapsed_time}')
