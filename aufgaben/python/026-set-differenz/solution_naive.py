"""
Naive Loesung mit O(n*m)-Lookup.
"""


def ohne(a: list, b: list) -> list:
    ergebnis: list = []
    for x in a:
        if x not in b and x not in ergebnis:
            ergebnis.append(x)
    return ergebnis
