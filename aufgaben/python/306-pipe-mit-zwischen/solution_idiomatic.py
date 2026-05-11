_OPS = {
    "double": lambda x: x * 2,
    "square": lambda x: x ** 2,
    "negate": lambda x: -x,
    "increment": lambda x: x + 1,
    "absolute": abs,
}


def pipe_mit_zwischen(start, ops: list[str]) -> list:
    aktuell = start
    out: list = []
    for op in ops:
        if op in _OPS:
            aktuell = _OPS[op](aktuell)
        out.append(aktuell)
    return out
