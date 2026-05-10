"""
Naive Lösung: erstes Element merken, in Schleife vergleichen.
"""


def maximum(zahlen: list[int]) -> int | None:
    if not zahlen:
        return None
    groesstes = zahlen[0]
    for z in zahlen[1:]:
        if z > groesstes:
            groesstes = z
    return groesstes
