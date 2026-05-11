from itertools import combinations


def kombis(liste: list, k: int) -> list[list]:
    if k <= 0 or k > len(liste):
        return []
    return [list(t) for t in combinations(liste, k)]
