with open("da.txt", "w") as datei:
    datei.write("eins\nzwei\n")

name = input()
try:
    with open(name) as datei:
        anzahl = len(datei.readlines())
    print(name, "hat", anzahl, "Zeilen")
except FileNotFoundError:
    print(name, "gibt es nicht")
