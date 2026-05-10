"""
Pythonic: alle Summen in ein Set, prüfen, ob nur ein Wert drin steht.
"""


def ist_magisch(matrix: list[list[int]]) -> bool:
    n = len(matrix)
    if n == 0:
        return False
    summen: set = set()
    for zeile in matrix:
        summen.add(sum(zeile))
    for spalte in zip(*matrix):
        summen.add(sum(spalte))
    summen.add(sum(matrix[i][i] for i in range(n)))
    summen.add(sum(matrix[i][n - 1 - i] for i in range(n)))
    return len(summen) == 1
