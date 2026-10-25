with open("einkauf.txt", "w") as datei:
    while True:
        ware = input()
        if ware == "ende":
            break
        datei.write(ware + "\n")

with open("einkauf.txt") as datei:
    for nr, zeile in enumerate(datei, 1):
        print(f"{nr}. {zeile.strip()}")
