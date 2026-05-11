def zentrieren(text: str, breite: int, pad: str) -> str:
    if len(pad) != 1:
        return text
    if len(text) >= breite:
        return text
    return text.center(breite, pad)
