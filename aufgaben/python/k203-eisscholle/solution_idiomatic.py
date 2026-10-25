class Scholle:
    def __init__(self, breite, laenge):
        self.breite = breite
        self.laenge = laenge

    def flaeche(self):
        return self.breite * self.laenge

    def umfang(self):
        return 2 * (self.breite + self.laenge)


scholle = Scholle(int(input()), int(input()))
print("Fläche:", scholle.flaeche())
print("Umfang:", scholle.umfang())
