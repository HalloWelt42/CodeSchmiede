def zahl_addieren(a: str, b: str) -> str:
    i, j = len(a) - 1, len(b) - 1
    uebertrag = 0
    teile: list[str] = []
    while i >= 0 or j >= 0 or uebertrag:
        za = ord(a[i]) - ord("0") if i >= 0 else 0
        zb = ord(b[j]) - ord("0") if j >= 0 else 0
        s = za + zb + uebertrag
        teile.append(str(s % 10))
        uebertrag = s // 10
        i -= 1
        j -= 1
    return "".join(reversed(teile))
