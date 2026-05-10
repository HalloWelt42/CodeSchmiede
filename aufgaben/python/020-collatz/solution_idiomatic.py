"""
Idiomatische Loesung mit Bit-Trick: `n & 1` ist genau dann 1, wenn n
ungerade ist. Spart das `% 2` und liest sich kompakt.
"""


def collatz_laenge(n: int) -> int:
    schritte = 0
    while n != 1:
        n = n // 2 if n & 1 == 0 else 3 * n + 1
        schritte += 1
    return schritte
