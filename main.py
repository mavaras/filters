import sys
import time
import cv2
from typ import Palette
from modules import (
    vangogh,
    vaporize,
    glitches
)
from utils import (
    randomize_strokes_order
)


PROGRESS_LIMIT = 100
IMG_PATH = sys.argv[1] if len(sys.argv) != 1 else 'imgs/me.jpeg'

def main():
    img = cv2.imread(IMG_PATH)
    # grid = randomize_strokes_order(img)
    area = {
        'x': 50,
        'y': 80,
        'width': 150,
        'height': 150,
    }
    img_res = glitches.glitch(img, area=area.values())
    #img_res = vangogh.vangogh(img)

    cv2.imshow('img_res', img_res)
    cv2.waitKey(0)


if __name__ == '__main__':
    start_time = time.time()
    main()
    elapsed_time = time.time() - start_time
    print(f'execution time: {elapsed_time}')
