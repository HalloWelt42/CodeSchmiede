def takt(lage):
    hier = lage.etage
    gerufen = lage.rufe[1] | lage.rufe[-1]
    if lage.tuer == "offen":
        if lage.lichtschranke or hier in gerufen:
            return "warten"
        return "zu"
    if hier in gerufen or hier in lage.ziele:
        return "auf"
    if gerufen or lage.ziele:
        return "hoch" if hier == 0 else "runter"
    return "warten"
