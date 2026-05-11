def ip_zerlegen(s: str) -> list[int]:
    teile = s.split(".")
    if len(teile) != 4:
        return []
    out: list[int] = []
    for t in teile:
        if not t or not t.isdigit():
            return []
        n = int(t)
        if not 0 <= n <= 255:
            return []
        out.append(n)
    return out
