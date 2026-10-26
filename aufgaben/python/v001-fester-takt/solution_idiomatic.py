# Ein Umlauf: (Sekunden, Autos, Fußgänger)
PLAN = [(16, "gruen", "rot"), (3, "gelb", "rot"), (2, "rot", "rot"),
        (8, "rot", "gruen"), (3, "rot", "rot"), (1, "rotgelb", "rot")]
UMLAUF = sum(dauer for dauer, _, _ in PLAN)


def takt(lage):
    t = lage.sekunde % UMLAUF
    for dauer, auto, fuss in PLAN:
        if t < dauer:
            return {"auto": auto, "fuss": fuss}
        t -= dauer
