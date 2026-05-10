"""
Naive Lösung: alle Teiler von 1 bis n-1 durchprobieren und summieren.
"""


def ist_perfekt(n: int) -> bool:
    if n < 2:
        return False
    summe = 0
    for i in range(1, n):
        if n % i == 0:
            summe += i
    return summe == n
