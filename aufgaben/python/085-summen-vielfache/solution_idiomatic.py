def summe_vielfache(n: int, teiler: list[int]) -> int:
    vielfache: set[int] = set()
    for t in teiler:
        if t == 0:
            continue
        vielfache.update(range(t, n, t))
    return sum(vielfache)
