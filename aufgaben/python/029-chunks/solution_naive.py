"""
Klassische for-Schleife mit Schrittweite n.
"""


def chunks(liste: list, n: int) -> list[list]:
    ergebnis: list[list] = []
    for i in range(0, len(liste), n):
        ergebnis.append(liste[i:i + n])
    return ergebnis
