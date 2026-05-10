"""
Idiomatische Lösung: Generator-Ausdruck mit `sum()`. Lesbar, kurz,
schnell -- so schreibt man das in Python.
"""


def vokale_zaehlen(text: str) -> int:
    return sum(1 for c in text.lower() if c in "aeiou")
