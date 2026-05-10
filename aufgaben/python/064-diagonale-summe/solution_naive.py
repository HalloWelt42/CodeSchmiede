"""
Klassische Schleife.
"""


def diagonal_summen(matrix: list[list[int]]) -> list[int]:
    n = len(matrix)
    haupt = 0
    neben = 0
    for i in range(n):
        haupt += matrix[i][i]
        neben += matrix[i][n - 1 - i]
    return [haupt, neben]
