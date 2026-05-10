"""
Klassische doppelte Schleife.
"""


def transponieren(matrix: list[list]) -> list[list]:
    if not matrix or not matrix[0]:
        return []
    m = len(matrix)
    n = len(matrix[0])
    ergebnis: list[list] = []
    for j in range(n):
        zeile: list = []
        for i in range(m):
            zeile.append(matrix[i][j])
        ergebnis.append(zeile)
    return ergebnis
