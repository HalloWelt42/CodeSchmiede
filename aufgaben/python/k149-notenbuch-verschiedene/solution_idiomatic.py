titel = "Mein Notenbuch"
print(f"=== {titel.upper()} ===")
noten = {}
while True:
    fach = input()
    if fach == "ende":
        break
    noten[fach] = int(input())
for fach, note in noten.items():
    print(f"{fach}: {note}")
print("Verschiedene Noten:", sorted(set(noten.values())))
schnitt = sum(noten.values()) / len(noten)
print("Durchschnitt:", schnitt)
if schnitt <= 1.5:
    print("Urteil: sehr gut")
elif schnitt <= 2.5:
    print("Urteil: gut")
elif schnitt <= 3.5:
    print("Urteil: befriedigend")
elif schnitt <= 4:
    print("Urteil: ausreichend")
else:
    print("Urteil: nicht bestanden")
print("Sterne: ", end="")
for i in range(7 - round(schnitt)):
    print("*", end="")
print()
