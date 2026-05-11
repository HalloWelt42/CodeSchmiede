def hanoi(n: int, von: str = "A", ueber: str = "B", nach: str = "C") -> list:
    if n == 0:
        return []
    return (
        hanoi(n - 1, von, nach, ueber)
        + [[von, nach]]
        + hanoi(n - 1, ueber, von, nach)
    )
