"""
Optimale Loesung: nur bis sqrt(n) suchen, Teiler-Paare nutzen.
O(sqrt(n)) statt O(n).
"""


def ist_perfekt(n: int) -> bool:
    if n < 2:
        return False
    summe = 1  # 1 ist immer Teiler
    i = 2
    while i * i <= n:
        if n % i == 0:
            summe += i
            partner = n // i
            if partner != i:
                summe += partner
        i += 1
    return summe == n
