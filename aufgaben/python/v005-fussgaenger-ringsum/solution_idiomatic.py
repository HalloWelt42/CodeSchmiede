# Autos: je Phase Nord-Süd, Ost-West, Mindestdauer
PHASEN = {
    "ns": ("gruen", "rot", 10),
    "ns_gelb": ("gelb", "rot", 3),
    "ns_raeumen": ("rot", "rot", 2),
    "ow_an": ("rot", "rotgelb", 1),
    "ow": ("rot", "gruen", 8),
    "ow_gelb": ("rot", "gelb", 3),
    "ow_raeumen": ("rot", "rot", 2),
    "ns_an": ("rotgelb", "rot", 1),
}
FOLGE = list(PHASEN)
# Fußgänger gehen mit dem Verkehr, dessen Weg sie nicht kreuzen
PARALLEL = {"fuss_ow": "ns", "fuss_ns": "ow"}
GEHEN = 7
phase, seit = "ns", 0
gehen = {"fuss_ns": 0, "fuss_ow": 0}


def bereit(lage):
    if phase == "ns":
        return (lage.schleife["ow"] or lage.taster["fuss_ns"]) and not gehen["fuss_ow"]
    if phase == "ow":
        weiter = lage.schleife["ow"] and seit < 20
        return not weiter and not gehen["fuss_ns"]
    if phase == "ns_raeumen":
        return lage.frei["ow"]
    if phase == "ow_raeumen":
        return lage.frei["ns"]
    return True


def takt(lage):
    global phase, seit
    if seit >= PHASEN[phase][2] and bereit(lage):
        phase, seit = FOLGE[(FOLGE.index(phase) + 1) % len(FOLGE)], 0
    seit += 1
    for fuss, mit in PARALLEL.items():
        if gehen[fuss]:
            gehen[fuss] -= 1
        elif phase == mit and lage.taster[fuss] and lage.frei[fuss]:
            gehen[fuss] = GEHEN
    ns, ow, _ = PHASEN[phase]
    signale = {"ns": ns, "ow": ow}
    for fuss in PARALLEL:
        signale[fuss] = "gruen" if gehen[fuss] else "rot"
    return signale
