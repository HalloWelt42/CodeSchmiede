def _ist_prim(k: int) -> bool:
    if k < 2:
        return False
    if k < 4:
        return True
    if k % 2 == 0:
        return False
    i = 3
    while i * i <= k:
        if k % i == 0:
            return False
        i += 2
    return True


def goldbach_paar(n: int):
    if n <= 2 or n % 2 != 0:
        return None
    for p in range(2, n // 2 + 1):
        if _ist_prim(p) and _ist_prim(n - p):
            return [p, n - p]
    return None
