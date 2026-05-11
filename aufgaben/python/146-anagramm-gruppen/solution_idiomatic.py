from collections import defaultdict


def anagramm_gruppen(woerter: list[str]) -> list[list[str]]:
    gruppen: dict[str, list[str]] = defaultdict(list)
    for w in woerter:
        gruppen["".join(sorted(w))].append(w)
    return sorted([sorted(g) for g in gruppen.values()])
