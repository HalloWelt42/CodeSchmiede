from itertools import combinations


def potenzmenge(liste: list) -> list[list]:
    return [
        list(t)
        for k in range(len(liste) + 1)
        for t in combinations(liste, k)
    ]
