ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def zurueck(geheim, wort):
    raus, i = [], 0
    for c in geheim:
        if c in ABC:
            c = ABC[(ABC.index(c) - ABC.index(wort[i % len(wort)])) % 26]
            i += 1
        raus.append(c)
    return "".join(raus)


def verschiebung(spalte):
    # wie in Level 1: die Verschiebung, nach der die Spalte am deutschesten aussieht
    return max(range(26), key=lambda n: sum(DEUTSCH[ABC[(ABC.index(c) - n) % 26]] for c in spalte))


def knacke_laenge(geheim, laenge):
    buchstaben = [c for c in geheim if c in ABC]
    wort = "".join(ABC[verschiebung(buchstaben[i::laenge])] for i in range(laenge))
    return zurueck(geheim, wort)


def koinzidenz(spalte):
    n = len(spalte)
    return sum(spalte.count(c) * (spalte.count(c) - 1) for c in ABC) / (n * (n - 1))


def knacke(geheim):
    buchstaben = [c for c in geheim if c in ABC]
    for laenge in range(1, 16):
        spalten = [buchstaben[i::laenge] for i in range(laenge)]
        if sum(map(koinzidenz, spalten)) / laenge > 0.06:
            return knacke_laenge(geheim, laenge)
    return geheim
