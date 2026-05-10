"""
Klassische Schleife mit Zähler.
"""


def zaehle_gross(text: str) -> int:
    anzahl = 0
    for zeichen in text:
        if zeichen.isupper():
            anzahl += 1
    return anzahl
