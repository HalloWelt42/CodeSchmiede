def map_range(x: float, a1: float, a2: float, b1: float, b2: float) -> float:
    if a1 == a2:
        return b1
    y = b1 + (x - a1) * (b2 - b1) / (a2 - a1)
    return round(y, 4)
