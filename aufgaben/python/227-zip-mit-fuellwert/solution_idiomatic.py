from itertools import zip_longest


def zip_fuell(a: list, b: list, fuell) -> list[list]:
    return [list(p) for p in zip_longest(a, b, fillvalue=fuell)]
