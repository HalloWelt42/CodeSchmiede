def paare(liste: list) -> list[list]:
    return [list(p) for p in zip(liste[::2], liste[1::2])]
