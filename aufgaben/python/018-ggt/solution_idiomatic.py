"""
Euklidischer Algorithmus, iterativ und idiomatisch in Python.
"""


def ggt(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a
