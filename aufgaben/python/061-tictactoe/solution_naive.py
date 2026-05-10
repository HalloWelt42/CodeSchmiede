"""
Klassische Linien-Prüfung mit if-Kette.
"""


def gewinner(brett: list[list[str]]) -> str:
    # Zeilen
    for i in range(3):
        if brett[i][0] == brett[i][1] == brett[i][2] != ".":
            return brett[i][0]
    # Spalten
    for j in range(3):
        if brett[0][j] == brett[1][j] == brett[2][j] != ".":
            return brett[0][j]
    # Diagonalen
    if brett[0][0] == brett[1][1] == brett[2][2] != ".":
        return brett[0][0]
    if brett[0][2] == brett[1][1] == brett[2][0] != ".":
        return brett[0][2]
    return "."
