import sys
import time
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
    area = {
        'x': 0,
        'y': 0,
        'width': 270,
        'height': 500,
    }
    img_res = glitches.abstract_glitch(img, area=area.values())
    #img_res = vangogh.vangogh(img)
    if ARGS.write_output:
        cv2.imwrite(f'outimgs/out_{uuid.uuid4()}.jpg', img_res)
    cv2.imshow('img_res', img_res)
    cv2.waitKey(0)


if __name__ == '__main__':
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f'execution time: {elapsed_time}')
