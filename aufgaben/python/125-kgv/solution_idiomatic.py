from functools import reduce
from math import lcm


def kgv_liste(zahlen: list[int]) -> int:
    if not zahlen:
        return 0
    return reduce(lcm, zahlen, 1)
