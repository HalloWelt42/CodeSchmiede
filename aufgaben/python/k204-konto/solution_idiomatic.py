class Konto:
    def __init__(self, inhaber):
        self.inhaber = inhaber
        self.stand = 0

    def einzahlen(self, betrag):
        self.stand += betrag

    def abheben(self, betrag):
        if betrag > self.stand:
            print("Zu wenig Geld")
        else:
            self.stand -= betrag


konto = Konto("Pia")
while True:
    text = input()
    if text == "ende":
        break
    betrag = int(text)
    if betrag >= 0:
        konto.einzahlen(betrag)
    else:
        konto.abheben(-betrag)
print(konto.inhaber, "hat", konto.stand)
