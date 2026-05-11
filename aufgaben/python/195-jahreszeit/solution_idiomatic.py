_JAHRESZEITEN = [
    "ungueltig",
    "winter", "winter", "fruehling",
    "fruehling", "fruehling", "sommer",
    "sommer", "sommer", "herbst",
    "herbst", "herbst", "winter",
]


def jahreszeit(monat: int) -> str:
    if 1 <= monat <= 12:
        return _JAHRESZEITEN[monat]
    return "ungueltig"
