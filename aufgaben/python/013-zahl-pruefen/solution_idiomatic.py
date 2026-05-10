"""
Idiomatische Lösung: nur bis sqrt(n) prüfen + 2 als Sonderfall.
O(sqrt(n)) -- für n=997 nur 30 Iterationen statt 995.
"""

from math import isqrt


def ist_primzahl(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for teiler in range(3, isqrt(n) + 1, 2):
        if n % teiler == 0:
            return False
    return True
