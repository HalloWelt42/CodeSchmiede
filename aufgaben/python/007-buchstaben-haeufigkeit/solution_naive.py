"""
Naive Lösung: explizite Schleife mit dict.get-Fallback.
"""


def buchstaben_haeufigkeit(text: str) -> dict[str, int]:
    ergebnis: dict[str, int] = {}
    for c in text:
        if c in ergebnis:
            ergebnis[c] += 1
        else:
            ergebnis[c] = 1
    return ergebnis
