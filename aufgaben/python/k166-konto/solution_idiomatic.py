konto = 100


def abheben(betrag):
    global konto
    if betrag > konto:
        print("Zu wenig Geld")
    else:
        konto -= betrag


while True:
    betrag = int(input())
    if betrag == 0:
        break
    abheben(betrag)
print("Stand:", konto)
