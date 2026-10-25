preise = {"Hering": 3, "Eis": 2, "Lachs": 6}
summe = 0
while True:
    ware = input()
    if ware == "kasse":
        break
    try:
        summe += preise[ware]
    except KeyError:
        print("Unbekannt:", ware)
print("Summe:", summe)
