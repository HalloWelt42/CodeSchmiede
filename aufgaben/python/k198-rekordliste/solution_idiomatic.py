def speichern(rekorde, dateiname):
    with open(dateiname, "w") as datei:
        for name, punkte in rekorde.items():
            datei.write(f"{name};{punkte}\n")


def laden(dateiname):
    rekorde = {}
    with open(dateiname) as datei:
        for zeile in datei:
            name, punkte = zeile.strip().split(";")
            rekorde[name] = int(punkte)
    return rekorde


rekorde = {}
while True:
    name = input()
    if name == "ende":
        break
    punkte = int(input())
    if punkte > rekorde.get(name, 0):
        rekorde[name] = punkte
speichern(rekorde, "rekorde.txt")
geladen = laden("rekorde.txt")
bester = ""
for name, punkte in geladen.items():
    print(f"{name}: {punkte}")
    if bester == "" or punkte > geladen[bester]:
        bester = name
print("Bester:", bester)
