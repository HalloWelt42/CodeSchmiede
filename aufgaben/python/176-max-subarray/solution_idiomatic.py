def max_summe(zahlen: list[int]) -> int:
    if not zahlen:
        return 0
    akt = bestes = zahlen[0]
    for x in zahlen[1:]:
        akt = max(x, akt + x)
        bestes = max(bestes, akt)
    return bestes
