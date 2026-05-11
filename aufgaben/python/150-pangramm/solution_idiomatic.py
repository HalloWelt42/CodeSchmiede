_ALPHABET = set("abcdefghijklmnopqrstuvwxyz")


def ist_pangramm(text: str) -> bool:
    return _ALPHABET <= set(text.lower())
