import math


class Shape:
    def flaeche(self) -> float:
        return 0.0


class Kreis(Shape):
    def __init__(self, r: float) -> None:
        self.r = r

    def flaeche(self) -> float:
        return math.pi * self.r ** 2 if self.r > 0 else 0.0


class Rechteck(Shape):
    def __init__(self, b: float, h: float) -> None:
        self.b, self.h = b, h

    def flaeche(self) -> float:
        if self.b <= 0 or self.h <= 0:
            return 0.0
        return self.b * self.h


class Dreieck(Shape):
    def __init__(self, a: float, b: float, c: float) -> None:
        self.a, self.b, self.c = a, b, c

    def flaeche(self) -> float:
        if min(self.a, self.b, self.c) <= 0:
            return 0.0
        seiten = sorted([self.a, self.b, self.c])
        if seiten[0] + seiten[1] <= seiten[2]:
            return 0.0
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


def _baue(spec: list) -> Shape:
    typ = spec[0]
    if typ == "kreis":
        return Kreis(spec[1])
    if typ == "rechteck":
        return Rechteck(spec[1], spec[2])
    if typ == "dreieck":
        return Dreieck(spec[1], spec[2], spec[3])
    return Shape()


def gesamt_flaeche(shapes: list) -> float:
    return round(sum(_baue(s).flaeche() for s in shapes), 2)
