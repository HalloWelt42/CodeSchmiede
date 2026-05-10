"""
Greedy mit zwei parallelen Listen.
"""


def int_zu_roemisch(n: int) -> str:
    werte = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbole = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    ergebnis = ""
    for i, w in enumerate(werte):
        while n >= w:
            ergebnis += symbole[i]
            n -= w
    return ergebnis
