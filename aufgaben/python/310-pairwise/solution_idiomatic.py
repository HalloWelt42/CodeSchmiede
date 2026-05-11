def pairwise(a: list) -> list[list]:
    def gen():
        for i in range(len(a) - 1):
            yield [a[i], a[i + 1]]
    return list(gen())
