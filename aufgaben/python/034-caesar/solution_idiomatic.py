"""
Helper extrahiert die Verschiebung; "".join mit Generator ist
idiomatisch und schneller als String-Konkatenation.
"""


def _verschiebe(c: str, k: int) -> str:
    if c.isupper():
        basis = ord("A")
    elif c.islower():
        basis = ord("a")
    else:
        return c
    return chr((ord(c) - basis + k) % 26 + basis)


def caesar(text: str, k: int) -> str:
    return "".join(_verschiebe(c, k) for c in text)
