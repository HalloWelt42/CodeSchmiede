with open("gruss.txt", "w") as datei:
    datei.write("Hallo Datei\n")

with open("gruss.txt") as datei:
    print(datei.read())
