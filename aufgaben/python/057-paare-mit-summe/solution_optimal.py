"""
Optimal mit Counter: O(n).
"""

from collections import Counter


def paare_anzahl(zahlen: list[int], ziel: int) -> int:
    zaehler = Counter(zahlen)
    anzahl = 0
    for wert, n in zaehler.items():
        partner = ziel - wert
        if partner == wert:
            anzahl += n * (n - 1) // 2
        elif partner > wert:
            anzahl += n * zaehler.get(partner, 0)
    return anzahl
