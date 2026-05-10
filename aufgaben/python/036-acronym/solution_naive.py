"""
Klassische Schleife.
"""


def akronym(text: str) -> str:
    ergebnis = ""
    for wort in text.split():
        if wort:
            ergebnis += wort[0].upper()
    return ergebnis
