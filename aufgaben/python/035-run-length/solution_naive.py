"""
Klassische Schleife mit aktuellem Zeichen + Zaehler.
"""


def rle(text: str) -> str:
    if not text:
        return ""
    ergebnis = ""
    aktuell = text[0]
    anzahl = 1
    for c in text[1:]:
        if c == aktuell:
            anzahl += 1
        else:
            ergebnis += aktuell + (str(anzahl) if anzahl > 1 else "")
            aktuell = c
            anzahl = 1
    ergebnis += aktuell + (str(anzahl) if anzahl > 1 else "")
    return ergebnis
