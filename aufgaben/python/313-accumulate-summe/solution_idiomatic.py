def laufende_summen(liste: list[int]) -> list[int]:
    def gen():
        summe = 0
        for x in liste:
            summe += x
            yield summe
    return list(gen())
