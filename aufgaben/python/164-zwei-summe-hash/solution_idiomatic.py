def zwei_summe(zahlen: list[int], ziel: int) -> list[int]:
    gesehen: dict[int, int] = {}
    for i, x in enumerate(zahlen):
        rest = ziel - x
        if rest in gesehen:
            return [gesehen[rest], i]
        gesehen[x] = i
    return []
