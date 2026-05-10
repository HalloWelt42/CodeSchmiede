"""
Naive Lösung: doppelte verschachtelte Schleife. O(n*m).
"""


def schnittmenge(a: list, b: list) -> list:
    ergebnis: list = []
    for x in a:
        if x in b and x not in ergebnis:
            ergebnis.append(x)
    return ergebnis
