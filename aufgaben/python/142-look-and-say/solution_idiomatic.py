from itertools import groupby


def look_and_say(n: int) -> str:
    s = "1"
    for _ in range(n - 1):
        s = "".join(f"{len(list(g))}{z}" for z, g in groupby(s))
    return s
