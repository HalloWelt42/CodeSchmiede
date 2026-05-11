def diagonal_summen(matrix: list[list[int]]) -> list[int]:
    if not matrix or not matrix[0] or len(matrix) != len(matrix[0]):
        return [0, 0]
    n = len(matrix)
    haupt = sum(matrix[i][i] for i in range(n))
    neben = sum(matrix[i][n - 1 - i] for i in range(n))
    return [haupt, neben]
