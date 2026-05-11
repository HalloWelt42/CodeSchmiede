class Konto:
    def __init__(self, saldo: int) -> None:
        self.saldo = saldo

    def buchen(self, betrag: int) -> int:
        self.saldo += betrag
        return self.saldo


def konto_saldi(start: int, buchungen: list[int]) -> list[int]:
    konto = Konto(start)
    return [konto.buchen(b) for b in buchungen]
