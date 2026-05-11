def addiere_zu_allen(c: int, liste: list[int]) -> list[int]:
    add_c = lambda x: x + c
    return [add_c(x) for x in liste]
