"""
Optimierte Lösung: Counter-Vergleich, O(n) -- linear statt sortiert.
Bei sehr langen Strings spürbar schneller.
"""

from collections import Counter


def ist_anagramm(a: str, b: str) -> bool:
    return Counter(a) == Counter(b)
