def zentroid(punkte: list[list]) -> list[float]:
    if not punkte:
        return [0.0, 0.0]
    n = len(punkte)
    cx = sum(p[0] for p in punkte) / n
    cy = sum(p[1] for p in punkte) / n
    return [round(cx, 4), round(cy, 4)]
