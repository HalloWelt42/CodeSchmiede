"""
Naive Lösung: Probiere alle Teiler ab 2 bis n und entferne sie so oft
wie möglich. Korrekt, aber langsam fuer grosse Primzahlen.
"""


def primfaktoren(n: int) -> list[int]:
    faktoren: list[int] = []
    i = 2
    while i <= n:
        while n % i == 0:
            faktoren.append(i)
            n //= i
        i += 1
    return faktoren
