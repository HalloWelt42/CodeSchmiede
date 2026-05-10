"""
Idiomatische Lösung: sortierte Buchstaben-Listen vergleichen.
Eine Zeile, klar lesbar, O(n log n).
"""


def ist_anagramm(a: str, b: str) -> bool:
    return sorted(a) == sorted(b)
