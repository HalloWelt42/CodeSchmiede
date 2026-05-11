def memoize_lauf(eingaben: list[int]) -> list:
    cache: dict[int, int] = {}
    out: list = []
    for x in eingaben:
        if x in cache:
            out.append([cache[x], True])
        else:
            wert = x * x
            cache[x] = wert
            out.append([wert, False])
    return out
