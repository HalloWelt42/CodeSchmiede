"""
Naive Loesung -- k mal jeweils das erste Element ans Ende verschieben.
"""


def rotiere(liste: list, k: int) -> list:
    if not liste:
        return []
    ergebnis = list(liste)
    k = k % len(ergebnis)
    for _ in range(k):
        ergebnis.append(ergebnis.pop(0))
    return ergebnis
