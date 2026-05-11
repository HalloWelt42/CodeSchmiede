def drop_while_null(liste: list[int]) -> list[int]:
    def gen():
        dropping = True
        for x in liste:
            if dropping and x == 0:
                continue
            dropping = False
            yield x
    return list(gen())
