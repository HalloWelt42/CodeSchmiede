"""
Idiomatisch mit sum() -- ein Einzeiler.
"""


def mittelwert(zahlen: list[float]) -> float:
    if not zahlen:
        return 0.0
    return sum(zahlen) / len(zahlen)
