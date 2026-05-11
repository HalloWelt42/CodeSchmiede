def skalar_mal(matrix: list[list], c) -> list[list]:
    return [[c * x for x in zeile] for zeile in matrix]
