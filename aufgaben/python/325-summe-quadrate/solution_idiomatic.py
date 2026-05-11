def summe_quadrate(n: int) -> int:
    if n <= 0:
        return 0
    return n * (n + 1) * (2 * n + 1) // 6
