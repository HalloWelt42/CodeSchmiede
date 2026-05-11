def aus_ziffern(ziffern: list[int]) -> int:
    n = 0
    for d in ziffern:
        n = 10 * n + d
    return n
