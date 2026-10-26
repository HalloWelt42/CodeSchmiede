# Je Phase: Signal für Autos, Signal für Fußgänger, Mindestdauer in Sekunden
PHASEN = {
    "autos": ("gruen", "rot", 20),
    "gelb": ("gelb", "rot", 3),
    "raeumen": ("rot", "rot", 2),
    "gehen": ("rot", "gruen", 8),
    "leeren": ("rot", "rot", 3),
    "anfahren": ("rotgelb", "rot", 1),
}
WEITER = {"autos": "gelb", "gelb": "raeumen", "raeumen": "gehen",
          "gehen": "leeren", "leeren": "anfahren", "anfahren": "autos"}
phase, seit = "autos", 0


def bereit(lage):
    if phase == "autos":
        return lage.taster
    if phase == "raeumen":
        return lage.frei["fuss"]
    return True


def takt(lage):
    global phase, seit
    if seit >= PHASEN[phase][2] and bereit(lage):
        phase, seit = WEITER[phase], 0
    seit += 1
    auto, fuss, _ = PHASEN[phase]
    return {"auto": auto, "fuss": fuss}
