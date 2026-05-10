"""
Iterative Lösung mit klassischer for-Schleife.
"""


def fakultaet(n: int) -> int:
    ergebnis = 1
    for i in range(2, n + 1):
        ergebnis *= i
    return ergebnis
