richtung = {}  # je Kabine: 1 hoch, -1 runter, 0 steht


def zustaendig(lage, e):
    """Gehört der Ruf in Etage e dieser Kabine? Dann ist sie am nächsten dran (bei Gleichstand der kleinere Name)."""
    abstand = {name: (abs(k.etage - e), name) for name, k in lage.aufzuege.items()}
    return min(abstand, key=abstand.get) == lage.aufzug


def takt(lage):
    hier = lage.etage
    r = richtung.get(lage.aufzug, 0)
    alle_rufe = lage.rufe[1] | lage.rufe[-1]
    if lage.tuer == "offen":
        return "warten" if lage.lichtschranke or (hier in alle_rufe and not lage.voll) else "zu"
    meine = {d: {e for e in lage.rufe[d] if zustaendig(lage, e)} for d in (1, -1)}
    if lage.voll:
        meine = {1: set(), -1: set()}
    if hier in lage.ziele or hier in meine.get(r, set()):
        return "auf"
    alles = meine[1] | meine[-1] | lage.ziele
    if not any((e - hier) * r > 0 for e in alles):
        r = 1 if any(e > hier for e in alles) else -1 if any(e < hier for e in alles) else 0
        if hier in meine[1] | meine[-1]:
            richtung[lage.aufzug] = r
            return "auf"
        if r == 0 and hier > 0:
            r = -1  # nichts zu tun: ins EG
    richtung[lage.aufzug] = r
    return {1: "hoch", -1: "runter", 0: "warten"}[r]
