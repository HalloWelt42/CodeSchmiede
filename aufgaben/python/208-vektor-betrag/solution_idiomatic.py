import math


def betrag(v: list) -> float:
    return round(math.sqrt(sum(x * x for x in v)), 4)
