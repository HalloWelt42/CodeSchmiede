def dezimal_zu_binaer(n: int) -> str:
    if n == 0:
        return "0"
    teile: list[str] = []
    while n > 0:
        teile.append(str(n % 2))
        n //= 2
    return "".join(reversed(teile))
