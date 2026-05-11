from math import comb


def binomial(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    return comb(n, k)
