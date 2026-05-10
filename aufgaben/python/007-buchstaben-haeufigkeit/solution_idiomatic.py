"""
Idiomatische Lösung: collections.Counter ist genau dafür gemacht.
"""

from collections import Counter


def buchstaben_haeufigkeit(text: str) -> dict[str, int]:
    return dict(Counter(text))
