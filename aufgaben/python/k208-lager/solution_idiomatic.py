class Lager:
    def __init__(self):
        self.bestand = {}

    def einlagern(self, ware, anzahl):
        self.bestand[ware] = self.bestand.get(ware, 0) + anzahl

    def entnehmen(self, ware, anzahl):
        if self.bestand.get(ware, 0) < anzahl:
            raise ValueError(f"Zu wenig {ware}")
        self.bestand[ware] -= anzahl


lager = Lager()
while True:
    befehl = input()
    if befehl == "ende":
        break
    art, ware, anzahl = befehl.split()
    try:
        if art == "rein":
            lager.einlagern(ware, int(anzahl))
        else:
            lager.entnehmen(ware, int(anzahl))
    except ValueError as fehler:
        print(fehler)
for ware, anzahl in lager.bestand.items():
    print(f"{ware}: {anzahl}")
