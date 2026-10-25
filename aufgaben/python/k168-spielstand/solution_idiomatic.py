punkte = 0
leben = 3


def treffer():
    global punkte
    punkte += 10


def daneben():
    global leben
    leben -= 1


while True:
    zug = input()
    if zug == "ende":
        break
    if zug == "t":
        treffer()
    else:
        daneben()
    if leben == 0:
        print("Spiel vorbei")
        break
print(f"Punkte: {punkte}, Leben: {leben}")
