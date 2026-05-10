"""
Optimale Loesung: Bricht die Schleife ab, sobald i*i > n -- der Rest
ist dann selbst eine Primzahl. Das macht den Algorithmus auf O(sqrt(n))
fuer grosse Primzahlen.
"""


def primfaktoren(n: int) -> list[int]:
    faktoren: list[int] = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            faktoren.append(i)
            n //= i
        i += 1
    if n > 1:
        faktoren.append(n)
    return faktoren
