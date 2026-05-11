import math
from collections import namedtuple

Punkt = namedtuple("Punkt", ["x", "y"])


def punkt_paar_info(x1: float, y1: float, x2: float, y2: float) -> list[float]:
    a = Punkt(x1, y1)
    b = Punkt(x2, y2)
    distanz = math.hypot(b.x - a.x, b.y - a.y)
    mid_x = (a.x + b.x) / 2
    mid_y = (a.y + b.y) / 2
    return [round(distanz, 4), round(mid_x, 4), round(mid_y, 4)]
