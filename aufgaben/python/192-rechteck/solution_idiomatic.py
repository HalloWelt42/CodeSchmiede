import math


def rechteck(b: float, h: float) -> list[float]:
    if b <= 0 or h <= 0:
        return [0, 0, 0]
    return [
        round(b * h, 2),
        round(2 * (b + h), 2),
        round(math.sqrt(b * b + h * h), 2),
    ]
