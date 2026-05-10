"""
Klassische Schleife.
"""


def snake_zu_camel(text: str) -> str:
    teile = text.split("_")
    if not teile:
        return ""
    ergebnis = teile[0]
    for t in teile[1:]:
        ergebnis += t.capitalize()
    return ergebnis
