def runde_zu_vielfache(n: int, k: int) -> int:
    if k <= 0:
        return n
    return round(n / k) * k
