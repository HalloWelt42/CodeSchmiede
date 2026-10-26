MIN, MAX, AUSFALL = 6, 20, 25

zustand, gruppe, ziel, seit = "gruen", "ns", None, 0


def naechste(lage):
    if lage.einsatz:
        return None if gruppe == lage.einsatz else lage.einsatz
    if gruppe == "ns":
        if lage.stoerung == "ow":
            # Schleife gestört: Ost-West kommt regelmäßig dran
            return "ow" if seit > AUSFALL else None
        return "ow" if lage.schleife["ow"] else None
    # Ost-West behält Grün, solange Autos kommen
    return None if lage.schleife["ow"] and seit <= MAX else "ns"


def takt(lage):
    global zustand, gruppe, ziel, seit
    seit += 1
    if zustand == "nacht":
        if not lage.nacht:
            zustand, ziel, seit = "raeumen", "ns", 1
    elif zustand == "gruen" and lage.nacht:
        zustand, ziel, seit = "gelb", None, 1
    elif zustand == "gruen" and (seit > MIN or lage.einsatz):
        ziel = naechste(lage)
        if ziel:
            zustand, seit = "gelb", 1
    elif zustand == "gelb" and seit > 3:
        zustand, seit = ("raeumen" if ziel else "nacht"), 1
    elif zustand == "raeumen" and lage.nacht:
        zustand, seit = "nacht", 1
    elif zustand == "raeumen" and seit > 2 and lage.frei[ziel]:
        zustand, seit = "an", 1
    elif zustand == "an" and seit > 1:
        zustand, gruppe, seit = "gruen", ziel, 1

    if zustand == "nacht":
        return {"ns": "gelb_blinkt", "ow": "gelb_blinkt"}
    signale = {"ns": "rot", "ow": "rot"}
    if zustand in ("gruen", "gelb"):
        signale[gruppe] = zustand
    elif zustand == "an":
        signale[ziel] = "rotgelb"
    return signale
