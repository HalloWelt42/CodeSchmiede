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


eintraege = 0


def eintragen(fach, note):
    global eintraege
    eintraege += 1
    if fach in noten:
        print(f"{fach} überschrieben")
    noten[fach] = note


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


titel = "Mein Notenbuch"
print(f"=== {titel.upper()} ===")
noten = {}
while True:
    fach = input()
    if fach == "ende":
        break
    try:
        eintragen(fach, lies_note(input()))
    except ValueError as fehler:
        print("Übersprungen:", fehler)
print("Einträge:", eintraege)
for fach, note in noten.items():
    print(f"{fach}: {note} ({urteil(note)})")
print("Verschiedene Noten:", sorted(set(noten.values())))
schnitt = sum(noten.values()) / len(noten)
print("Durchschnitt:", schnitt)
print("Median:", median(noten.values()))
print("Urteil:", urteil(schnitt))
print("Sterne:", sterne(schnitt))
speichern(noten, "notenbuch.txt")
print("Geladen:", laden("notenbuch.txt"))
