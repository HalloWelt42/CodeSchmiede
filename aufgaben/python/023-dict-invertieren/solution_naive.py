"""
Klassische Schleife.
"""


def invertiere(d: dict) -> dict:
    ergebnis: dict = {}
    for schluessel, wert in d.items():
        ergebnis[str(wert)] = schluessel
    return ergebnis
