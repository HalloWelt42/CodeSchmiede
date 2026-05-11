def fibs_bis(max_wert: int) -> list[int]:
    def gen():
        a, b = 0, 1
        while a <= max_wert:
            yield a
            a, b = b, a + b
    return list(gen())
