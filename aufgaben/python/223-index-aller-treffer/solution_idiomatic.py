def alle_indizes(liste: list, wert) -> list[int]:
    return [i for i, x in enumerate(liste) if x == wert]
