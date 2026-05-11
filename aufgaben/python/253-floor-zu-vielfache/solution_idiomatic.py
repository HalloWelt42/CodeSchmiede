def floor_vielfache(n: int, k: int) -> int:
    if k <= 0:
        return n
    return n // k * k
