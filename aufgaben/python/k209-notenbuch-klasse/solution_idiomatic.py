from statistics import median


def urteil(note):
    if note <= 1.5:
        return "sehr gut"
    elif note <= 2.5:
        return "gut"
    elif note <= 3.5:
        return "befriedigend"
    elif note <= 4:
        return "ausreichend"
    else:
        return "nicht bestanden"


def sterne(note):
    return "*" * (7 - round(note))


def lies_note(text):
    try:
        note = int(text)
    except ValueError:
        raise ValueError(f"{text} ist keine Zahl")
    if note < 1 or note > 6:
        raise ValueError(f"{note} ist keine Note")
    return note


def speichern(noten, dateiname):
    with open(dateiname, "w") as datei:
        for fach, note in noten.items():
            datei.write(f"{fach};{note}\n")


def laden(dateiname):
    geladen = {}
    with open(dateiname) as datei:
        for zeile in datei:
            fach, note = zeile.strip().split(";")
            geladen[fach] = int(note)
    return geladen


class Notenbuch:
    def __init__(self, titel):
        self.titel = titel
        self.noten = {}
        self.eintraege = 0

    def eintragen(self, fach, note):
        self.eintraege += 1
        if fach in self.noten:
            print(f"{fach} überschrieben")
        self.noten[fach] = note

    def schnitt(self):
        return sum(self.noten.values()) / len(self.noten)

    def bestes_fach(self):
        bestes = ""
        for fach, note in self.noten.items():
            if bestes == "" or note < self.noten[bestes]:
                bestes = fach
        return bestes


buch = Notenbuch("Mein Notenbuch")
print(f"=== {buch.titel.upper()} ===")
while True:
    fach = input()
    if fach == "ende":
        break
    try:
        buch.eintragen(fach, lies_note(input()))
    except ValueError as fehler:
        print("Übersprungen:", fehler)
print("Einträge:", buch.eintraege)
for fach, note in buch.noten.items():
    print(f"{fach}: {note} ({urteil(note)})")
print("Verschiedene Noten:", sorted(set(buch.noten.values())))
print("Durchschnitt:", buch.schnitt())
print("Median:", median(buch.noten.values()))
print("Urteil:", urteil(buch.schnitt()))
print("Sterne:", sterne(buch.schnitt()))
print("Bestes Fach:", buch.bestes_fach())
speichern(buch.noten, "notenbuch.txt")
print("Geladen:", laden("notenbuch.txt"))
