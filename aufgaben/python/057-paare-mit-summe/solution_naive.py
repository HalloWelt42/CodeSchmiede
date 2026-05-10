"""
Naive Loesung: doppelte Schleife. O(n^2).
"""


def paare_anzahl(zahlen: list[int], ziel: int) -> int:
    n = len(zahlen)
    anzahl = 0
    for i in range(n):
        for j in range(i + 1, n):
            if zahlen[i] + zahlen[j] == ziel:
                anzahl += 1
    return anzahl
