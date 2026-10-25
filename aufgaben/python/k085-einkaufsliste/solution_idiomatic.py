anzahl = 0
while True:
    sache = input()
    if sache == "fertig":
        break
    print("-", sache)
    anzahl += 1
print("Anzahl:", anzahl)
