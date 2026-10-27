ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def schiebe(text, n):
    return "".join(ABC[(ABC.index(c) + n) % 26] if c in ABC else c for c in text)


def punkte(text):
    return sum(DEUTSCH.get(c, 0) for c in text)


def knacke(geheim):
    return max((schiebe(geheim, -n) for n in range(26)), key=punkte)
