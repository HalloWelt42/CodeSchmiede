titel = "Mein Notenbuch"
faecher = "Mathe, Deutsch, Musik"
print(f"=== {titel.upper()} ===")
print("Fächer:", faecher)
summe = 0
anzahl = 0
while True:
    note = int(input())
    if note == 0:
        break
    summe += note
    anzahl += 1
schnitt = summe / anzahl
print("Noten:", anzahl)
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
