import math


def dreieck_winkel(a: float, b: float, c: float) -> str:
    if min(a, b, c) <= 0:
        return "ungueltig"
    seiten = sorted([a, b, c])
    aa, bb, cc = seiten
    if aa + bb <= cc:
        return "ungueltig"
    summe = aa * aa + bb * bb
    quadrat = cc * cc
    if math.isclose(summe, quadrat):
        return "recht"
    if quadrat < summe:
        return "spitz"
    return "stumpf"
