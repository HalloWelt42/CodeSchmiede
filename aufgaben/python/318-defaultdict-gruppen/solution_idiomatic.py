from collections import defaultdict


def gruppiere_anfang(strings: list[str]) -> dict:
    gruppen: dict[str, list[str]] = defaultdict(list)
    for s in strings:
        if not s:
            continue
        gruppen[s[0].lower()].append(s)
    return {k: sorted(v) for k, v in sorted(gruppen.items())}
