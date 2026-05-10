"""
Naive Lösung: explizite Schleife mit Zähler-Variable.
"""


def vokale_zaehlen(text: str) -> int:
    anzahl = 0
    for c in text.lower():
        if c in "aeiou":
            anzahl += 1
    return anzahl
