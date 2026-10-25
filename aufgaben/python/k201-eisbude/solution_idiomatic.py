class Eisbude:
    def __init__(self, ort):
        self.ort = ort
        self.kugeln = 0


bude = Eisbude("Strand")
bude.kugeln = 12
print(bude.ort, bude.kugeln)
