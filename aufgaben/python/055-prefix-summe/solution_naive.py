"""
Klassisch mit Akkumulator-Schleife.
"""


def prefix_summe(zahlen: list[int]) -> list[int]:
    summe = 0
    ergebnis: list[int] = []
    for x in zahlen:
        summe += x
        ergebnis.append(summe)
    return ergebnis
