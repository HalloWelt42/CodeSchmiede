import math


def geometrisches_mittel(zahlen: list[float]) -> float:
    if not zahlen:
        return 0.0
    if any(x <= 0 for x in zahlen):
        return 0.0
    return round(math.prod(zahlen) ** (1 / len(zahlen)), 4)
