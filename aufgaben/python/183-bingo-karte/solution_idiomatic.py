def hat_bingo(karte: list[list[int]], gezogen: list[int]) -> bool:
    g = set(gezogen)
    n = len(karte)
    if n == 0:
        return False
    for i in range(n):
        if all(z in g for z in karte[i]):
            return True
    for j in range(n):
        if all(karte[i][j] in g for i in range(n)):
            return True
    if all(karte[i][i] in g for i in range(n)):
        return True
    if all(karte[i][n - 1 - i] in g for i in range(n)):
        return True
    return False
