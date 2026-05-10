"""
Mit Lookup-Tabelle als Konstante.
"""


_TAGE = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def _ist_schaltjahr(jahr: int) -> bool:
    return (jahr % 4 == 0 and jahr % 100 != 0) or jahr % 400 == 0


def tage_im_monat(jahr: int, monat: int) -> int:
    if monat < 1 or monat > 12:
        return 0
    if monat == 2 and _ist_schaltjahr(jahr):
        return 29
    return _TAGE[monat]
