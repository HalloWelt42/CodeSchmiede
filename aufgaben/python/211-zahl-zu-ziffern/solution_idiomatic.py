def zu_ziffern(n: int) -> list[int]:
    return [int(c) for c in str(abs(n))]
