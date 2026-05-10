"""
Idiomatische Lösung mit Mapping + Slicing für die Fünfer-Gruppen.
"""


def atbash_codiere(text: str) -> str:
    teile: list[str] = []
    for c in text.lower():
        if c.isalpha():
            teile.append(chr(ord("a") + (25 - (ord(c) - ord("a")))))
        elif c.isdigit():
            teile.append(c)
    flach = "".join(teile)
    return " ".join(flach[i:i + 5] for i in range(0, len(flach), 5))
