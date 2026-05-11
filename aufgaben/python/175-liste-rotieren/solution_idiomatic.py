def rotieren(a: list, k: int) -> list:
    n = len(a)
    if n == 0:
        return []
    k %= n
    if k == 0:
        return list(a)
    return list(a[-k:]) + list(a[:-k])
