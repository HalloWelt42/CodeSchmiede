def hamming_distanz(a: str, b: str) -> int:
    if len(a) != len(b):
        return -1
    return sum(1 for x, y in zip(a, b) if x != y)
