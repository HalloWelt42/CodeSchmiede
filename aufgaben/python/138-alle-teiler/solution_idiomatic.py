def alle_teiler(n: int) -> list[int]:
    if n < 1:
        return []
    teiler: set[int] = set()
    i = 1
    while i * i <= n:
        if n % i == 0:
            teiler.add(i)
            teiler.add(n // i)
        i += 1
    return sorted(teiler)
