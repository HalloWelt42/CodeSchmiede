"""
Naive Lösung: explizite Schleife mit Akkumulator-Variable.
"""


def summe(zahlen: list[int]) -> int:
    ergebnis = 0
    for z in zahlen:
        ergebnis += z
    return ergebnis
