def digitale_wurzel(n: int) -> int:
    if n == 0:
        return 0
    return 1 + (n - 1) % 9
