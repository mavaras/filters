from typ import Image as ImageType
from modules.vaporize.vaporize_domain import draw_vaporize


CASCADE_FOLDER = 'res/cascade'

def vaporize(img: ImageType) -> ImageType:

    return draw_vaporize(img)
