def _ist_sublist(klein: list, gross: list) -> bool:
    if not klein:
        return True
    n, m = len(klein), len(gross)
    if n > m:
        return False
    return any(gross[i:i + n] == klein for i in range(m - n + 1))


def vergleiche(a: list, b: list) -> str:
    if a == b:
        return "gleich"
    if _ist_sublist(a, b):
        return "sublist"
    if _ist_sublist(b, a):
        return "superlist"
    return "ungleich"
