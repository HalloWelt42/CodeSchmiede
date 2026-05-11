_SCHLAEGT = {"stein": "schere", "schere": "papier", "papier": "stein"}


def gewinner(zug1: str, zug2: str) -> str:
    if zug1 not in _SCHLAEGT or zug2 not in _SCHLAEGT:
        return "ungueltig"
    if zug1 == zug2:
        return "unentschieden"
    return "spieler1" if _SCHLAEGT[zug1] == zug2 else "spieler2"
