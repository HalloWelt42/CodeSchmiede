"""
Naive Loesung: alle Teiler bis min(a, b) durchprobieren und das groesste
gemeinsame Ergebnis merken. Funktioniert, ist aber langsam fuer grosse
Zahlen.
"""


def ggt(a: int, b: int) -> int:
    if a == 0:
        return b
    if b == 0:
        return a
    groesster = 1
    for k in range(1, min(a, b) + 1):
        if a % k == 0 and b % k == 0:
            groesster = k
    return groesster
