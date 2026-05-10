"""
Idiomatisch mit bisect aus der Standardbibliothek.
"""

from bisect import bisect_left


def binaere_suche(liste: list[int], ziel: int) -> int:
    pos = bisect_left(liste, ziel)
    if pos != len(liste) and liste[pos] == ziel:
        return pos
    return -1
