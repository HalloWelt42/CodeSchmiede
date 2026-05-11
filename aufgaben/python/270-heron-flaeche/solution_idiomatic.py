import math


def dreieck_flaeche(a: float, b: float, c: float) -> float:
    if min(a, b, c) <= 0:
        return 0.0
    seiten = sorted([a, b, c])
    if seiten[0] + seiten[1] <= seiten[2]:
        return 0.0
    s = (a + b + c) / 2
    return round(math.sqrt(s * (s - a) * (s - b) * (s - c)), 4)
