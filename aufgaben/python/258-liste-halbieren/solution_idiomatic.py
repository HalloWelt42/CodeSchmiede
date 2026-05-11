def halbieren(liste: list) -> list[list]:
    mid = len(liste) // 2
    return [list(liste[:mid]), list(liste[mid:])]
