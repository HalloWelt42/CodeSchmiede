def primzahlen_bis(n: int) -> list[int]:
    def gen():
        if n < 2:
            return
        sieb = [True] * (n + 1)
        sieb[0] = sieb[1] = False
        for i in range(2, n + 1):
            if sieb[i]:
                yield i
                for j in range(i * i, n + 1, i):
                    sieb[j] = False
    return list(gen())
