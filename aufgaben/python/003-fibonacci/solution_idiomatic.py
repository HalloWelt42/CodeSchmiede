"""
Idiomatische Loesung: iterativ mit Tuple-Swap. Lineare Laufzeit O(n),
konstanter Speicher. Klassischer Python-Stil.
"""


def fibonacci(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
