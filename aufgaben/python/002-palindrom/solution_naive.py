"""
Naive Loesung: explizite Schleife, Vergleich Zeichen fuer Zeichen.
"""


def ist_palindrom(text: str) -> bool:
    laenge = len(text)
    for i in range(laenge // 2):
        if text[i] != text[laenge - 1 - i]:
            return False
    return True
