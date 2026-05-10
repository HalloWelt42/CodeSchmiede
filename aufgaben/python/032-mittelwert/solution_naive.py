"""
Klassisch mit Schleife.
"""


def mittelwert(zahlen: list[float]) -> float:
    if not zahlen:
        return 0.0
    summe = 0.0
    for x in zahlen:
        summe += x
    return summe / len(zahlen)
