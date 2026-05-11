def im_bereich_zaehlen(zahlen: list, a, b) -> int:
    return sum(1 for x in zahlen if a <= x <= b)
