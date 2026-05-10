"""
Naive Lösung: doppelte Schleife. O(n^2).
"""


def two_sum(zahlen: list[int], ziel: int) -> list[int]:
    n = len(zahlen)
    for i in range(n):
        for j in range(i + 1, n):
            if zahlen[i] + zahlen[j] == ziel:
                return [i, j]
    return []
