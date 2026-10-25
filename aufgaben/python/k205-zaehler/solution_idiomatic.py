class Zaehler:
    def __init__(self):
        self.stand = 0

    def klick(self):
        self.stand += 1

    def zuruecksetzen(self):
        self.stand = 0


zaehler = Zaehler()
while True:
    befehl = input()
    if befehl == "ende":
        break
    if befehl == "klick":
        zaehler.klick()
    else:
        zaehler.zuruecksetzen()
print("Stand:", zaehler.stand)
