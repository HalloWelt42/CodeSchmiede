"""
Idiomatische Loesung: String-Slicing mit Schrittweite -1 kehrt den
String um. Vergleich mit Originalstring liefert das Ergebnis direkt.
"""


def ist_palindrom(text: str) -> bool:
    return text == text[::-1]
