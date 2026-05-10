"""
Klassische Schleife mit String-Konkatenation.
"""


def camel_zu_snake(text: str) -> str:
    ergebnis = ""
    for i, c in enumerate(text):
        if c.isupper() and i > 0:
            ergebnis += "_"
        ergebnis += c.lower()
    return ergebnis
