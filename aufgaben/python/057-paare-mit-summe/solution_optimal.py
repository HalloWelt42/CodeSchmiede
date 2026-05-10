"""
Optimal mit Counter: O(n).
"""

from collections import Counter


def paare_anzahl(zahlen: list[int], ziel: int) -> int:
    zähler = Counter(zahlen)
    anzahl = 0
    for wert, n in zähler.items():
        partner = ziel - wert
        if partner == wert:
            anzahl += n * (n - 1) // 2
        elif partner > wert:
            anzahl += n * zähler.get(partner, 0)
    return anzahl
