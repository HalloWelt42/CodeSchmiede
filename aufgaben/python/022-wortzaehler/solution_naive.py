"""
Naive Lösung mit explizitem if/else fuer den ersten Eintrag eines
Wortes.
"""


def wortzaehler(text: str) -> dict[str, int]:
    zaehlung: dict[str, int] = {}
    for wort in text.split():
        if wort in zaehlung:
            zaehlung[wort] += 1
        else:
            zaehlung[wort] = 1
    return zaehlung
