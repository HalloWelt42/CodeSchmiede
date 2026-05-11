def rle_decode(s: str) -> str:
    teile: list[str] = []
    zahl = ""
    for c in s:
        if c.isdigit():
            zahl += c
        else:
            teile.append(c * int(zahl))
            zahl = ""
    return "".join(teile)
