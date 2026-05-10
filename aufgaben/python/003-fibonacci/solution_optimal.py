"""
Optimierte Loesung: rekursiv mit Memoisierung via functools.lru_cache.
Behaelt die lesbare rekursive Definition, gewinnt aber lineare Laufzeit
durch Caching der Zwischenergebnisse.
"""

from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
