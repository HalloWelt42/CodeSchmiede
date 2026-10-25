class Angler:
    def __init__(self, name, fang):
        self.name = name
        self.fang = fang


angler = []
while True:
    name = input()
    if name == "ende":
        break
    angler.append(Angler(name, int(input())))
sieger = angler[0]
summe = 0
for a in angler:
    summe += a.fang
    if a.fang > sieger.fang:
        sieger = a
print("Sieger:", sieger.name, "mit", sieger.fang)
print("Durchschnitt:", summe / len(angler))
