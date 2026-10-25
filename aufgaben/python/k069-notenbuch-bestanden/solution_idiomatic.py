titel = "Mein Notenbuch"
faecher = "Mathe, Deutsch, Musik"
print(f"=== {titel.upper()} ===")
print("Fächer:", faecher)
mathe = int(input())
deutsch = int(input())
musik = int(input())
schnitt = (mathe + deutsch + musik) / 3
print("Durchschnitt:", schnitt)
print("Bestanden:", schnitt <= 4)
