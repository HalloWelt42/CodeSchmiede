def zu_dezimal(b: str) -> int:
    n = 0
    for c in b:
        n = 2 * n + int(c)
    return n
