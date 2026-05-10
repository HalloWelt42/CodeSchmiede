"""
Klassische Schleife mit Zaehler.
"""


def zaehle_gross(text: str) -> int:
    anzahl = 0
    for zeichen in text:
        if zeichen.isupper():
            anzahl += 1
    return anzahl
