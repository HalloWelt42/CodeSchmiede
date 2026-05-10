"""
Klassische Schleife: Ziffern extrahieren, einzeln potenzieren.
"""


def ist_armstrong(n: int) -> bool:
    s = str(n)
    k = len(s)
    summe = 0
    for c in s:
        summe += int(c) ** k
    return summe == n
