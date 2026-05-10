"""
Rekursive Lösung -- folgt der mathematischen Definition.
"""


def potenz(basis: int, exponent: int) -> int:
    if exponent == 0:
        return 1
    return basis * potenz(basis, exponent - 1)
