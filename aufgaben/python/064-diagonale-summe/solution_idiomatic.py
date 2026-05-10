"""
Pythonic mit sum + Generator.
"""


def diagonal_summen(matrix: list[list[int]]) -> list[int]:
    n = len(matrix)
    return [
        sum(matrix[i][i] for i in range(n)),
        sum(matrix[i][n - 1 - i] for i in range(n)),
    ]
