def matmul(a: list[list], b: list[list]) -> list[list]:
    if not a or not b or not a[0] or not b[0]:
        return []
    n = len(a[0])
    if len(b) != n:
        return []
    m, p = len(a), len(b[0])
    c = [[0] * p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            c[i][j] = sum(a[i][k] * b[k][j] for k in range(n))
    return c
