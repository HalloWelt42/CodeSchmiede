_OPS = {
    "double": lambda x: x * 2,
    "square": lambda x: x ** 2,
    "negate": lambda x: -x,
    "increment": lambda x: x + 1,
    "absolute": abs,
}


def pipeline(liste: list, ops: list[str]) -> list:
    aktuell = list(liste)
    for op in ops:
        if op in _OPS:
            aktuell = [_OPS[op](x) for x in aktuell]
    return aktuell
