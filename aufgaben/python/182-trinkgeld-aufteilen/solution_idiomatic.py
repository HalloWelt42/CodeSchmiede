def pro_person(rechnung: float, tip_prozent: float, personen: int) -> float:
    if personen <= 0 or rechnung < 0:
        return 0.0
    gesamt = rechnung * (1 + tip_prozent / 100)
    return round(gesamt / personen, 2)
