class Bankkonto:
    def __init__(self, saldo: float, zinssatz_prozent: float) -> None:
        self.saldo = saldo
        self.zinssatz = zinssatz_prozent / 100

    def zinsen_buchen(self) -> float:
        self.saldo += self.saldo * self.zinssatz
        return self.saldo


def jahres_endsaldi(start: float, zinssatz_prozent: float, jahre: int) -> list[float]:
    konto = Bankkonto(start, zinssatz_prozent)
    return [round(konto.zinsen_buchen(), 2) for _ in range(jahre)]
