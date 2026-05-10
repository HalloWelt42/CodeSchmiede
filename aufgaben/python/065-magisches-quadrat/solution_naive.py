"""
Klassisch: alle Summen einzeln berechnen, dann vergleichen.
"""


def ist_magisch(matrix: list[list[int]]) -> bool:
    n = len(matrix)
    if n == 0:
        return False
    ziel = sum(matrix[0])
    # Zeilen
    for zeile in matrix:
        if sum(zeile) != ziel:
            return False
    # Spalten
    for j in range(n):
        s = 0
        for i in range(n):
            s += matrix[i][j]
        if s != ziel:
            return False
    # Diagonalen
    haupt = sum(matrix[i][i] for i in range(n))
    neben = sum(matrix[i][n - 1 - i] for i in range(n))
    return haupt == ziel and neben == ziel
