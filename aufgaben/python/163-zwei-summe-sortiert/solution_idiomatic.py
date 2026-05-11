def zwei_summe_sortiert(zahlen: list[int], ziel: int) -> list[int]:
    links, rechts = 0, len(zahlen) - 1
    while links < rechts:
        s = zahlen[links] + zahlen[rechts]
        if s == ziel:
            return [links, rechts]
        if s < ziel:
            links += 1
        else:
            rechts -= 1
    return []
