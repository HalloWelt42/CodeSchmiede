"""
Idiomatische Lösung: dict.fromkeys() nutzt aus, dass dict-Schluessel
seit Python 3.7 in Insertion-Reihenfolge stehen und automatisch
eindeutig sind.
"""


def ohne_duplikate(zahlen: list) -> list:
    return list(dict.fromkeys(zahlen))
