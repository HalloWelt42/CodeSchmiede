def bit_anzahl(n: int) -> int:
    z = 0
    while n:
        n &= n - 1
        z += 1
    return z
