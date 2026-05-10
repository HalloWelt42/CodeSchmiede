"""
Naive Loesung mit linearer Teilersumme.
"""


def _teiler_summe(n: int) -> int:
    summe = 0
    for i in range(1, n):
        if n % i == 0:
            summe += i
    return summe


def sind_befreundet(a: int, b: int) -> bool:
    if a == b:
        return False
    return _teiler_summe(a) == b and _teiler_summe(b) == a
