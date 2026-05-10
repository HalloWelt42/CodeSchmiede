"""
Idiomatic mit zip(*matrix).
"""


def transponieren(matrix: list[list]) -> list[list]:
    return [list(zeile) for zeile in zip(*matrix)]
