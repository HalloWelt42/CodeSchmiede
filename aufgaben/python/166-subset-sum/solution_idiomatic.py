def subset_sum(zahlen: list[int], ziel: int) -> bool:
    erreichbar: set[int] = {0}
    for x in zahlen:
        erreichbar |= {s + x for s in erreichbar}
        if ziel in erreichbar:
            return True
    return ziel == 0
