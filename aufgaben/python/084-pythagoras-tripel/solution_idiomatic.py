def pythagoras_tripel(n: int) -> list[list[int]]:
    ergebnis: list[list[int]] = []
    for a in range(1, n // 3 + 1):
        for b in range(a + 1, (n - a) // 2 + 1):
            c = n - a - b
            if c > b and a * a + b * b == c * c:
                ergebnis.append([a, b, c])
    return ergebnis
