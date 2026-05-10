"""
Idiomatisch mit dict.get() -- liefert 0 als Default und vermeidet
die Sonderfall-Verzweigung.
"""


def wortzaehler(text: str) -> dict[str, int]:
    zaehlung: dict[str, int] = {}
    for wort in text.split():
        zaehlung[wort] = zaehlung.get(wort, 0) + 1
    return zaehlung
