def general_fizzbuzz(n: int, regeln: list[list]) -> list[str]:
    out: list[str] = []
    for i in range(1, n + 1):
        wort = "".join(w for (t, w) in regeln if i % t == 0)
        out.append(wort or str(i))
    return out
