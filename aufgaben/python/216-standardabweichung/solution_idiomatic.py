import math


def stdabw(zahlen: list[float]) -> float:
    n = len(zahlen)
    if n < 2:
        return 0.0
    mittel = sum(zahlen) / n
    varianz = sum((x - mittel) ** 2 for x in zahlen) / n
    return round(math.sqrt(varianz), 4)
