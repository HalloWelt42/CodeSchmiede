"""
Schnellere Teilersumme via sqrt(n)-Trick.
"""


def _teiler_summe(n: int) -> int:
    if n < 2:
        return 0
    summe = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            summe += i
            partner = n // i
            if partner != i:
                summe += partner
        i += 1
    return summe


def sind_befreundet(a: int, b: int) -> bool:
    if a == b:
        return False
    return _teiler_summe(a) == b and _teiler_summe(b) == a
