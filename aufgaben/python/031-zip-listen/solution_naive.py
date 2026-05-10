"""
Klassische Schleife mit min-Laenge plus Slicing fuer den Rest.
"""


def verzahne(a: list, b: list) -> list:
    ergebnis: list = []
    kurz = min(len(a), len(b))
    for i in range(kurz):
        ergebnis.append(a[i])
        ergebnis.append(b[i])
    ergebnis.extend(a[kurz:])
    ergebnis.extend(b[kurz:])
    return ergebnis
