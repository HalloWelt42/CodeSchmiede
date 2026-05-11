_STUECKELUNG = [200, 100, 50, 20, 10, 5, 2, 1]


def wechselgeld(cent: int) -> list[int]:
    out: list[int] = []
    for s in _STUECKELUNG:
        out.append(cent // s)
        cent %= s
    return out
