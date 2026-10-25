titel = "Mein Notenbuch"
faecher = "Mathe, Deutsch, Musik"
print(f"=== {titel.upper()} ===")
print("Fächer:", faecher)
mathe = int(input())
deutsch = int(input())
musik = int(input())
schnitt = (mathe + deutsch + musik) / 3
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
