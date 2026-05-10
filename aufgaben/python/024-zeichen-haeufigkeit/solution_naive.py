"""
Klassisches Dict-Zaehlen mit if/else.
"""


def zeichen_haeufigkeit(text: str) -> dict[str, int]:
    zaehlung: dict[str, int] = {}
    for zeichen in text:
        if zeichen in zaehlung:
            zaehlung[zeichen] += 1
        else:
            zaehlung[zeichen] = 1
    return zaehlung
