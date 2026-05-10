"""
Alle Linien als Liste von Tripeln durchgehen.
"""


def gewinner(brett: list[list[str]]) -> str:
    linien: list[list[str]] = []
    for i in range(3):
        linien.append(brett[i])
        linien.append([brett[0][i], brett[1][i], brett[2][i]])
    linien.append([brett[0][0], brett[1][1], brett[2][2]])
    linien.append([brett[0][2], brett[1][1], brett[2][0]])
    for linie in linien:
        if linie[0] == linie[1] == linie[2] != ".":
            return linie[0]
    return "."
