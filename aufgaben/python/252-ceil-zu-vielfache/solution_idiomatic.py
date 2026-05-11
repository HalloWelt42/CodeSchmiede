import math


def ceil_vielfache(n: int, k: int) -> int:
    if k <= 0:
        return n
    return math.ceil(n / k) * k
