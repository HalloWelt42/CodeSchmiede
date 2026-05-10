"""
Klassisch mit if-else-Kette.
"""


def _ist_schaltjahr(jahr: int) -> bool:
    return (jahr % 4 == 0 and jahr % 100 != 0) or jahr % 400 == 0


def tage_im_monat(jahr: int, monat: int) -> int:
    if monat < 1 or monat > 12:
        return 0
    if monat in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if monat in (4, 6, 9, 11):
        return 30
    return 29 if _ist_schaltjahr(jahr) else 28
