def zu_binaer(n: int) -> str:
    if n == 0:
        return "0"
    bits: list[str] = []
    while n > 0:
        bits.append(str(n % 2))
        n //= 2
    return "".join(reversed(bits))
