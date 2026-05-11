def take_while_positiv(liste: list[int]) -> list[int]:
    def gen():
        for x in liste:
            if x > 0:
                yield x
            else:
                break
    return list(gen())
