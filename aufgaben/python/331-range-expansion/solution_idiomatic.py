def bereich_entpacken(s: str) -> list[int]:
    if not s:
        return []
    out: list[int] = []
    for stueck in s.split(","):
        idx = stueck.find("-", 1)
        if idx > 0:
            a = int(stueck[:idx])
            b = int(stueck[idx + 1:])
            out.extend(range(a, b + 1))
        else:
            out.append(int(stueck))
    return out
