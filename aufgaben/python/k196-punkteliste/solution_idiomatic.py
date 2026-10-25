with open("punkte.txt", "w") as datei:
    datei.write("Pit;17\nPia;42\nPaul;8\n")

bester = ""
beste = 0
summe = 0
with open("punkte.txt") as datei:
    for zeile in datei:
        name, punkte = zeile.strip().split(";")
        punkte = int(punkte)
        summe += punkte
        if punkte > beste:
            bester, beste = name, punkte
print("Bester:", bester, "mit", beste)
print("Summe:", summe)
