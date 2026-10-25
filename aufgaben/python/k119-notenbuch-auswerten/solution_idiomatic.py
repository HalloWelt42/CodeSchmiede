titel = "Mein Notenbuch"
faecher = "Mathe, Deutsch, Musik"
print(f"=== {titel.upper()} ===")
print("Fächer:", faecher)
noten = []
while True:
    note = int(input())
    if note == 0:
        break
    noten.append(note)
schnitt = sum(noten) / len(noten)
print("Noten:", sorted(noten))
print("Beste:", min(noten), "Schlechteste:", max(noten))
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
