def alle_rotationen(liste: list) -> list[list]:
    return [list(liste[i:] + liste[:i]) for i in range(len(liste))]
