from enum import Enum
from typing import List
import numpy as np


Image = np.ndarray
Palette = List[List[str]]

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class GlitchTypes(Enum):
    ABSTRACT: str = 'abstract'
    CYCLE: str = 'cycle'
    COLORIZED: str = 'colorized'
