with open("gedicht.txt", "w") as datei:
    datei.write("Ein Pinguin im Schnee\n")
    datei.write("trinkt am Morgen Tee\n")
    datei.write("und ruft dann juchhe\n")

zeilen = 0
woerter = 0
with open("gedicht.txt") as datei:
    for zeile in datei:
        zeilen += 1
        woerter += len(zeile.split())
print("Zeilen:", zeilen)
print("Wörter:", woerter)
