# Reihe der Gruppen; dran ist die nächste, bei der jemand wartet (Nord-Süd wartet immer)
REIHE = ["ns", "ns_links", "ow", "ow_links", "fuss"]
MIN = {"fuss": 8}
MAX = 20
RAEUMEN = {"fuss": 3}

zustand, gruppe, ziel, seit = "gruen", "ns", None, 0


def wartet(lage, g):
    if g == "ns":
        return True
    return lage.taster[g] if g == "fuss" else lage.schleife[g]


def naechste(lage):
    if gruppe not in ("ns", "fuss") and lage.schleife[gruppe] and seit <= MAX:
        return None  # es kommen noch welche
    i = REIHE.index(gruppe)
    for g in REIHE[i + 1:] + REIHE[:i]:
        if wartet(lage, g):
            return g
    return None


def takt(lage):
    global zustand, gruppe, ziel, seit
    seit += 1
    if zustand == "gruen" and seit > MIN.get(gruppe, 6):
        ziel = naechste(lage)
        if ziel:
            zustand, seit = ("gelb" if gruppe != "fuss" else "raeumen"), 1
    elif zustand == "gelb" and seit > 3:
        zustand, seit = "raeumen", 1
    elif zustand == "raeumen" and seit > RAEUMEN.get(gruppe, 2) and lage.frei[ziel]:
        zustand, seit = ("an" if ziel != "fuss" else "gruen"), 1
        if ziel == "fuss":
            gruppe = ziel
    elif zustand == "an" and seit > 1:
        zustand, gruppe, seit = "gruen", ziel, 1
    signale = {g: "rot" for g in REIHE}
    if zustand in ("gruen", "gelb"):
        signale[gruppe] = zustand
    elif zustand == "an":
        signale[ziel] = "rotgelb"
    return signale
