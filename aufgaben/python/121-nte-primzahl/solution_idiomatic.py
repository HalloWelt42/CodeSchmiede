def _ist_prim(n: int) -> bool:
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def nte_primzahl(n: int) -> int:
    if n < 1:
        return -1
    gefunden = 0
    kandidat = 1
    while gefunden < n:
        kandidat += 1
        if _ist_prim(kandidat):
            gefunden += 1
    return kandidat
