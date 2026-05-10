from functools import reduce
from math import gcd


def ggt_liste(zahlen: list[int]) -> int:
    return reduce(gcd, zahlen, 0)
