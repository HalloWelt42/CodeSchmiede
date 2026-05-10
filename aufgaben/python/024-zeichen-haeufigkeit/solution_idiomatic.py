"""
Idiomatisch mit dict.get().
"""


def zeichen_haeufigkeit(text: str) -> dict[str, int]:
    zaehlung: dict[str, int] = {}
    for zeichen in text:
        zaehlung[zeichen] = zaehlung.get(zeichen, 0) + 1
    return zaehlung
