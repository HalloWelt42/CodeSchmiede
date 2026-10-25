with open("tage.txt", "w") as datei:
    datei.write("Montag\n")
with open("tage.txt", "a") as datei:
    datei.write("Dienstag\n")
with open("tage.txt") as datei:
    print(datei.read())
