"""
Doppelte Schleife mit append.
"""


def flatten(liste: list[list]) -> list:
    ergebnis: list = []
    for innen in liste:
        for x in innen:
            ergebnis.append(x)
    return ergebnis
