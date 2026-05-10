"""
Mit datetime aus der Standardbibliothek -- robust und kurz.
"""

from datetime import date


def wochentag(jahr: int, monat: int, tag: int) -> int:
    # date.weekday(): Mo=0..So=6. Wir wollen So=0..Sa=6.
    py_wt = date(jahr, monat, tag).weekday()
    return (py_wt + 1) % 7
