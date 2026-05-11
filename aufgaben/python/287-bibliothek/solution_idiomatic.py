class Bibliothek:
    def __init__(self, bestand: list[str]) -> None:
        self.buecher: set[str] = set(bestand)

    def leihen(self, titel: str) -> None:
        self.buecher.discard(titel)

    def zurueck(self, titel: str) -> None:
        self.buecher.add(titel)


def ausleihen(bestand: list[str], operationen: list) -> list[str]:
    bib = Bibliothek(bestand)
    for op in operationen:
        if op[0] == "leihen":
            bib.leihen(op[1])
        elif op[0] == "zurueck":
            bib.zurueck(op[1])
    return sorted(bib.buecher)
