def skalarprodukt(a: list, b: list):
    if len(a) != len(b):
        return 0
    return sum(x * y for x, y in zip(a, b))
