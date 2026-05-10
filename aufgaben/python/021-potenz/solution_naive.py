"""
Iterative Loesung: ergebnis startet bei 1, dann exponent-mal
multiplizieren.
"""


def potenz(basis: int, exponent: int) -> int:
    ergebnis = 1
    for _ in range(exponent):
        ergebnis *= basis
    return ergebnis
