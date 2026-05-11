import math


def kreis(r: float) -> list[float]:
    if r <= 0:
        return [0.0, 0.0]
    return [round(math.pi * r * r, 2), round(2 * math.pi * r, 2)]
