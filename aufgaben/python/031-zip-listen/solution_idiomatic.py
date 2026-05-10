"""
Mit zip + chain.from_iterable -- die Standard-Bibliothek erledigt fast
alles.
"""

from itertools import chain


def verzahne(a: list, b: list) -> list:
    paare = zip(a, b)
    verzahnt = list(chain.from_iterable(paare))
    rest = a[len(b):] if len(a) > len(b) else b[len(a):]
    return verzahnt + list(rest)
