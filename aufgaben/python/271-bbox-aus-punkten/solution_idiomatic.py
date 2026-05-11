def bbox(punkte: list[list]) -> list:
    if not punkte:
        return [0, 0, 0, 0]
    xs = [p[0] for p in punkte]
    ys = [p[1] for p in punkte]
    return [min(xs), min(ys), max(xs), max(ys)]
