from collections import Counter


def top_n(liste: list, n: int) -> list[list]:
    if n <= 0:
        return []
    c = Counter(liste)
    sortiert = sorted(c.items(), key=lambda x: (-x[1], x[0]))
    return [[wert, anzahl] for wert, anzahl in sortiert[:n]]
