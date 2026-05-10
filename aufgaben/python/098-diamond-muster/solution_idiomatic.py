def diamant(buchstabe: str) -> list[str]:
    n = ord(buchstabe) - ord("A")
    if n < 0:
        return []

    def zeile(i: int) -> str:
        c = chr(ord("A") + i)
        outer = " " * (n - i)
        if i == 0:
            return outer + c + outer
        inner = " " * (2 * i - 1)
        return outer + c + inner + c + outer

    oben = [zeile(i) for i in range(n + 1)]
    return oben + oben[-2::-1]
