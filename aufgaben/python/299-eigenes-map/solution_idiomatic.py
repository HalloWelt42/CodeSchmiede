_OPS = {
    "double": lambda x: x * 2,
    "square": lambda x: x ** 2,
    "negate": lambda x: -x,
    "increment": lambda x: x + 1,
    "absolute": abs,
}


def map_op(liste: list, op: str) -> list:
    if op not in _OPS:
        return list(liste)
    fn = _OPS[op]
    return [fn(x) for x in liste]
