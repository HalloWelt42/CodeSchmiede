"""
Pythonic mit zip + Comprehension.
"""


def spalten_summen(matrix: list[list[int]]) -> list[int]:
    return [sum(spalte) for spalte in zip(*matrix)]
