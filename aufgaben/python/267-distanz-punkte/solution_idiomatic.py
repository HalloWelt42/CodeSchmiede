import math


def distanz(p1: list, p2: list) -> float:
    return round(math.hypot(p2[0] - p1[0], p2[1] - p1[1]), 4)
