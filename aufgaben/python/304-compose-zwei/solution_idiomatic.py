_OPS = {
    "double": lambda x: x * 2,
    "square": lambda x: x ** 2,
    "negate": lambda x: -x,
    "increment": lambda x: x + 1,
    "absolute": abs,
}

_IDENTITY = lambda x: x


def compose_anwenden(x, f: str, g: str):
    fn_f = _OPS.get(f, _IDENTITY)
    fn_g = _OPS.get(g, _IDENTITY)
    return fn_g(fn_f(x))
