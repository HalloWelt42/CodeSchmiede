def zinseszins(kapital: float, zinssatz_prozent: float, jahre: int) -> float:
    return round(kapital * (1 + zinssatz_prozent / 100) ** jahre, 2)
