def glueckszahl(n: int) -> bool:
    gesehen: set[int] = set()
    while n != 1 and n not in gesehen:
        gesehen.add(n)
        n = sum(int(z) ** 2 for z in str(n))
    return n == 1
