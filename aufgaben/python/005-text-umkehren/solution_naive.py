"""
Naive Lösung: explizite Schleife rückwärts, baut neuen String auf.
"""


def text_umkehren(text: str) -> str:
    ergebnis = ""
    for i in range(len(text) - 1, -1, -1):
        ergebnis += text[i]
    return ergebnis
