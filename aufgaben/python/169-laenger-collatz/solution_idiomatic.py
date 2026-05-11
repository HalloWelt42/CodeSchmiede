def laengster_collatz(n: int) -> int:
    if n <= 1:
        return 0
    laenge: dict[int, int] = {1: 0}

    def L(k: int) -> int:
        weg: list[int] = []
        while k not in laenge:
            weg.append(k)
            k = k // 2 if k % 2 == 0 else 3 * k + 1
        basis = laenge[k]
        for i, x in enumerate(reversed(weg), 1):
            laenge[x] = basis + i
        return laenge[weg[0]] if weg else basis

    bester = 1
    beste_laenge = 0
    for s in range(1, n):
        ls = L(s)
        if ls > beste_laenge:
            bester, beste_laenge = s, ls
    return bester
