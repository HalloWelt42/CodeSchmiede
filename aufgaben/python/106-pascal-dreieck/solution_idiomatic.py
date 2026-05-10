def pascal(n: int) -> list[list[int]]:
    if n == 0:
        return []
    zeilen: list[list[int]] = [[1]]
    for _ in range(n - 1):
        vorher = zeilen[-1]
        neue = [1] + [a + b for a, b in zip(vorher, vorher[1:])] + [1]
        zeilen.append(neue)
    return zeilen
