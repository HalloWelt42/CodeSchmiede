"""
Naive Lösung: rekursiv. Exponentielle Laufzeit O(2^n) durch
mehrfaches Neuberechnen derselben Teilergebnisse.
Funktioniert, ist aber für n > 30 schon spürbar langsam.
"""


def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
