"""
Direkte Umsetzung der Regel mit if/else.
"""


def collatz_laenge(n: int) -> int:
    schritte = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        schritte += 1
    return schritte
