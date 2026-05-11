import re


def split_alles(text: str) -> list[str]:
    teile = re.split(r"[,;|\s]+", text)
    return [t for t in teile if t]
