"""
Idiomatische Lösung mit Bereinigung + Schleife.
"""


def ist_isbn_gueltig(isbn: str) -> bool:
    bereinigt = isbn.replace("-", "")
    if len(bereinigt) != 10:
        return False
    summe = 0
    for i, c in enumerate(bereinigt):
        if c == "X" and i == 9:
            wert = 10
        elif c.isdigit():
            wert = int(c)
        else:
            return False
        summe += wert * (10 - i)
    return summe % 11 == 0
