# Ein Umlauf: (Sekunden, Nord-Süd, Ost-West)
PLAN = [(14, "gruen", "rot"), (3, "gelb", "rot"), (2, "rot", "rot"), (1, "rot", "rotgelb"),
        (14, "rot", "gruen"), (3, "rot", "gelb"), (2, "rot", "rot"), (1, "rotgelb", "rot")]
UMLAUF = sum(dauer for dauer, _, _ in PLAN)


def takt(lage):
    t = lage.sekunde % UMLAUF
    for dauer, ns, ow in PLAN:
        if t < dauer:
            return {"ns": ns, "ow": ow}
        t -= dauer
