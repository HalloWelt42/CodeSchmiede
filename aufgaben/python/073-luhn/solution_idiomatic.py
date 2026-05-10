"""
Idiomatische Loesung: Whitespace strippen, prüfen ob nur Ziffern,
dann Luhn-Summe.
"""


def ist_luhn_gueltig(kandidat: str) -> bool:
    bereinigt = kandidat.replace(" ", "")
    if len(bereinigt) < 2 or not bereinigt.isdigit():
        return False
    summe = 0
    for i, c in enumerate(reversed(bereinigt)):
        ziffer = int(c)
        if i % 2 == 1:
            ziffer *= 2
            if ziffer > 9:
                ziffer -= 9
        summe += ziffer
    return summe % 10 == 0
