# Je Phase: Nord-Süd, Ost-West, Mindestdauer
PHASEN = {
    "ns": ("gruen", "rot", 10),
    "ns_gelb": ("gelb", "rot", 3),
    "ns_raeumen": ("rot", "rot", 2),
    "ow_an": ("rot", "rotgelb", 1),
    "ow": ("rot", "gruen", 6),
    "ow_gelb": ("rot", "gelb", 3),
    "ow_raeumen": ("rot", "rot", 2),
    "ns_an": ("rotgelb", "rot", 1),
}
FOLGE = list(PHASEN)
phase, seit = "ns", 0


def bereit(lage):
    if phase == "ns":
        return lage.schleife["ow"]
    if phase == "ow":
        # Grün behalten, solange Autos kommen, aber höchstens 20 s
        return not lage.schleife["ow"] or seit >= 20
    return True


def takt(lage):
    global phase, seit
    if seit >= PHASEN[phase][2] and bereit(lage):
        phase, seit = FOLGE[(FOLGE.index(phase) + 1) % len(FOLGE)], 0
    seit += 1
    ns, ow, _ = PHASEN[phase]
    return {"ns": ns, "ow": ow}
