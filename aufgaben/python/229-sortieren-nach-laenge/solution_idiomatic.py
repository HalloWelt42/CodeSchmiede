def nach_laenge(strings: list[str]) -> list[str]:
    return sorted(strings, key=lambda s: (len(s), s))
