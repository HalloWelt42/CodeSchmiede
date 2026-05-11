from collections import Counter


def haeufigster(zahlen: list):
    if not zahlen:
        return None
    c = Counter(zahlen)
    max_anzahl = max(c.values())
    return min(k for k, v in c.items() if v == max_anzahl)
