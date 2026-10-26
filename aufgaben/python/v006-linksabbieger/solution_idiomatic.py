GRUPPEN = ["ns", "ns_links", "ow"]
# wer nach wem drankommt, wenn dort jemand wartet; Nord-Süd ist immer dran
FOLGE = {"ns": ["ns_links", "ow"], "ns_links": ["ow", "ns"], "ow": ["ns"]}
MIN, MAX = 6, 20

zustand, gruppe, ziel, seit = "gruen", "ns", None, 0


def wartet(lage, g):
    return g == "ns" or lage.schleife[g]


def naechste(lage):
    if gruppe != "ns" and lage.schleife[gruppe] and seit <= MAX:
        return None  # es kommen noch welche
    return next((g for g in FOLGE[gruppe] if wartet(lage, g)), None)


def takt(lage):
    global zustand, gruppe, ziel, seit
    seit += 1
    if zustand == "gruen" and seit > MIN:
        ziel = naechste(lage)
        if ziel:
            zustand, seit = "gelb", 1
    elif zustand == "gelb" and seit > 3:
        zustand, seit = "raeumen", 1
    elif zustand == "raeumen" and seit > 2 and lage.frei[ziel]:
        zustand, seit = "an", 1
    elif zustand == "an" and seit > 1:
        zustand, gruppe, seit = "gruen", ziel, 1
    signale = {g: "rot" for g in GRUPPEN}
    if zustand in ("gruen", "gelb"):
        signale[gruppe] = zustand
    elif zustand == "an":
        signale[ziel] = "rotgelb"
    return signale
