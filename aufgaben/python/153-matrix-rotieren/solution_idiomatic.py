def rotieren(matrix: list[list]) -> list[list]:
    return [list(z) for z in zip(*matrix[::-1])]
