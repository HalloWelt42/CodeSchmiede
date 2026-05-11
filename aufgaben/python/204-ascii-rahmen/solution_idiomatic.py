def rahmen(zeilen: list[str]) -> list[str]:
    if not zeilen:
        return ["++", "++"]
    breite = max(len(z) for z in zeilen)
    if breite == 0:
        return ["++"] + ["||"] * len(zeilen) + ["++"]
    rand = "+" + "-" * (breite + 2) + "+"
    out = [rand]
    for z in zeilen:
        out.append(f"| {z.ljust(breite)} |")
    out.append(rand)
    return out
