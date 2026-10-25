fang = []


def notieren(fisch):
    fang.append(fisch)


while True:
    fisch = input()
    if fisch == "ende":
        break
    notieren(fisch)
print(fang)
print(len(fang), "Fische")
