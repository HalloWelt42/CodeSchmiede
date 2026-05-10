"""
Naive Lösung: jede Zahl einzeln auf Primalitaet prüfen.
Korrekt, aber langsam fuer grosse n.
"""


def _ist_prim(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def primzahlen_bis(n: int) -> list[int]:
    return [k for k in range(n + 1) if _ist_prim(k)]
