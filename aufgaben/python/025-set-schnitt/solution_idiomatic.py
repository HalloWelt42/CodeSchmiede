"""
Mit Sets: O(n+m) und liest sich klar.
"""


def schnittmenge(a: list, b: list) -> list:
    in_b = set(b)
    gesehen: set = set()
    ergebnis: list = []
    for x in a:
        if x in in_b and x not in gesehen:
            ergebnis.append(x)
            gesehen.add(x)
    return ergebnis
