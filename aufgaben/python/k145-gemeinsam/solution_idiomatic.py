pit = {"Vanille", "Erdbeer", "Nuss", "Zitrone"}
pia = {"Nuss", "Schoko", "Vanille"}
for sorte in sorted(pit & pia):
    print(sorte)
