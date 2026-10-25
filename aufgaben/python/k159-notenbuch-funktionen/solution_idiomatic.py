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


titel = "Mein Notenbuch"
print(f"=== {titel.upper()} ===")
noten = {}
while True:
    fach = input()
    if fach == "ende":
        break
    noten[fach] = int(input())
for fach, note in noten.items():
    print(f"{fach}: {note} ({urteil(note)})")
print("Verschiedene Noten:", sorted(set(noten.values())))
schnitt = sum(noten.values()) / len(noten)
print("Durchschnitt:", schnitt)
print("Urteil:", urteil(schnitt))
print("Sterne:", sterne(schnitt))
