"""
Idiomatische Lösung: `sorted()` mit `reverse=True` -- ein Aufruf,
ein neues sortiertes Ergebnis, Originalliste unverändert.
"""


def sortiere_absteigend(zahlen: list[int]) -> list[int]:
    return sorted(zahlen, reverse=True)
