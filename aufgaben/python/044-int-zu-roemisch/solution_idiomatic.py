"""
Wert-Symbol-Tupel + divmod -- so kompakt wie elegant.
"""


def int_zu_roemisch(n: int) -> str:
    paare = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
    ]
    teile: list[str] = []
    for wert, symbol in paare:
        anzahl, n = divmod(n, wert)
        teile.append(symbol * anzahl)
    return "".join(teile)
