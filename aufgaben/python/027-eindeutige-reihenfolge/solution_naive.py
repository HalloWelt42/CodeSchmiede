"""
Schleife mit gesehen-Set fuer schnellen Lookup.
"""


def eindeutige(a: list) -> list:
    gesehen: set = set()
    ergebnis: list = []
    for x in a:
        if x not in gesehen:
            ergebnis.append(x)
            gesehen.add(x)
    return ergebnis
