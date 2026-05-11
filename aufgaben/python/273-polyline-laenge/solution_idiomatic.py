import math


def polyline(punkte: list[list]) -> float:
    if len(punkte) < 2:
        return 0.0
    total = sum(
        math.hypot(p2[0] - p1[0], p2[1] - p1[1])
        for p1, p2 in zip(punkte, punkte[1:])
    )
    return round(total, 4)
