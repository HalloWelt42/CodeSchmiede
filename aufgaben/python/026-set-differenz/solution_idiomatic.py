"""
Mit Set-Lookup und Set-Tracking fuer Duplikate.
"""


def ohne(a: list, b: list) -> list:
    in_b = set(b)
    gesehen: set = set()
    ergebnis: list = []
    for x in a:
        if x not in in_b and x not in gesehen:
            ergebnis.append(x)
            gesehen.add(x)
    return ergebnis
