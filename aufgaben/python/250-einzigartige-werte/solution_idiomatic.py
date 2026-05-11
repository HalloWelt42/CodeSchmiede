from collections import Counter


def einzigartig(liste: list) -> list:
    c = Counter(liste)
    return sorted(k for k, v in c.items() if v == 1)
