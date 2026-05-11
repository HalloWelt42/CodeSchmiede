def letzte_n(liste: list, n: int) -> list:
    if n <= 0:
        return []
    return list(liste[-n:])
