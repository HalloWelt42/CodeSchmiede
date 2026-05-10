"""
Klassische doppelte Schleife.
"""


def spalten_summen(matrix: list[list[int]]) -> list[int]:
    if not matrix:
        return []
    n = len(matrix[0])
    summen = [0] * n
    for zeile in matrix:
        for j in range(n):
            summen[j] += zeile[j]
    return summen
