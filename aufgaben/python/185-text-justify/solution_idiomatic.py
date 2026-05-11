def ausrichten(text: str, breite: int, modus: str) -> str:
    if modus == "links":
        return text.ljust(breite)
    if modus == "rechts":
        return text.rjust(breite)
    if modus == "zentriert":
        return text.center(breite)
    return text
