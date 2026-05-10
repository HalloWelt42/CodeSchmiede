def rot(text: str, n: int) -> str:
    out: list[str] = []
    for c in text:
        if c.isupper():
            basis = ord("A")
        elif c.islower():
            basis = ord("a")
        else:
            out.append(c)
            continue
        out.append(chr((ord(c) - basis + n) % 26 + basis))
    return "".join(out)
