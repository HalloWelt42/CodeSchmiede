def dreieck_typ(a: float, b: float, c: float) -> str:
    if min(a, b, c) <= 0:
        return "ungueltig"
    seiten = sorted([a, b, c])
    if seiten[0] + seiten[1] <= seiten[2]:
        return "ungueltig"
    eindeutig = len({a, b, c})
    if eindeutig == 1:
        return "gleichseitig"
    if eindeutig == 2:
        return "gleichschenklig"
    return "ungleichseitig"
