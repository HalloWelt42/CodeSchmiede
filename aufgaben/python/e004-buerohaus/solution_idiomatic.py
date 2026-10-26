richtung = 0  # 1 hoch, -1 runter, 0 steht


def takt(lage):
    global richtung
    hier = lage.etage
    rufe = set() if lage.voll else lage.rufe[1] | lage.rufe[-1]
    if lage.tuer == "offen":
        return "warten" if lage.lichtschranke or hier in rufe else "zu"
    if hier in lage.ziele or (not lage.voll and hier in lage.rufe.get(richtung, set())):
        return "auf"
    alles = lage.rufe[1] | lage.rufe[-1] | lage.ziele
    if not any((e - hier) * richtung > 0 for e in alles):
        # vor uns liegt nichts mehr: neue Richtung, sonst zum Parken ins EG
        richtung = 1 if any(e > hier for e in alles) else -1 if any(e < hier for e in alles) else 0
        if hier in rufe:
            return "auf"
        if richtung == 0 and hier > 0:
            richtung = -1
    return {1: "hoch", -1: "runter", 0: "warten"}[richtung]
