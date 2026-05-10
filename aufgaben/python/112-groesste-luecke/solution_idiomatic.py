def groesste_luecke(zahlen: list[int]) -> int:
    if len(zahlen) < 2:
        return 0
    s = sorted(zahlen)
    return max(b - a for a, b in zip(s, s[1:]))
