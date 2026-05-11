from functools import reduce

_OPS = {
    "add": lambda a, x: a + x,
    "mul": lambda a, x: a * x,
    "max": max,
    "min": min,
}


def reduce_op(liste: list, op: str, start):
    if op not in _OPS:
        return start
    return reduce(_OPS[op], liste, start)
