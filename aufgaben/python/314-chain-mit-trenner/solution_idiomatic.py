def verketten_mit_trenner(listen: list[list], trenner) -> list:
    def gen():
        zuerst = True
        for liste in listen:
            if not liste:
                continue
            if not zuerst:
                yield trenner
            yield from liste
            zuerst = False
    return list(gen())
