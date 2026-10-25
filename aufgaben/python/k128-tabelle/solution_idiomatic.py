paare = []
while True:
    name = input()
    if name == "ende":
        break
    paare.append((name, int(input())))
summe = 0
for nr, (name, fang) in enumerate(paare, 1):
    print(nr, name, fang)
    summe += fang
print("Summe:", summe)
