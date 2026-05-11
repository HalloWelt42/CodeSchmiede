def harmonisches_mittel(zahlen: list[float]) -> float:
    if not zahlen:
        return 0.0
    if any(x <= 0 for x in zahlen):
        return 0.0
    return round(len(zahlen) / sum(1 / x for x in zahlen), 4)
