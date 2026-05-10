from collections import defaultdict


def gruppiere(woerter: list[str]) -> list[list[str]]:
    gruppen: dict[str, list[str]] = defaultdict(list)
    for w in woerter:
        schluessel = "".join(sorted(w.lower()))
        gruppen[schluessel].append(w)
    return sorted(sorted(g) for g in gruppen.values())
