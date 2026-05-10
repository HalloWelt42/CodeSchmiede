def ist_pangramm(text: str) -> bool:
    return set("abcdefghijklmnopqrstuvwxyz") <= set(text.lower())
