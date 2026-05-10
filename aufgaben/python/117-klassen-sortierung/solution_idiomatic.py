from collections import defaultdict


def sortiere_schueler(eintraege: list[dict]) -> dict[str, list[str]]:
    gruppen: dict[str, list[str]] = defaultdict(list)
    for e in eintraege:
        gruppen[str(e["klasse"])].append(e["name"])
    return {k: sorted(v) for k, v in gruppen.items()}
