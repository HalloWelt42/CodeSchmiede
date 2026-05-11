import math


def ist_quadratzahl(n: int) -> bool:
    if n < 0:
        return False
    w = math.isqrt(n)
    return w * w == n
