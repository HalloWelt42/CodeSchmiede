class Fisch:
    def __init__(self, art, gewicht):
        self.art = art
        self.gewicht = gewicht

    def __str__(self):
        return f"{self.art} ({self.gewicht} g)"


while True:
    art = input()
    if art == "ende":
        break
    print(Fisch(art, int(input())))
