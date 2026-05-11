def zaehler_bis(n: int) -> list[int]:
    def gen():
        for i in range(1, n + 1):
            yield i
    return list(gen())
