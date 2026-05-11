def alle_gleich(liste: list) -> bool:
    if not liste:
        return True
    erstes = liste[0]
    return all(x == erstes for x in liste)
