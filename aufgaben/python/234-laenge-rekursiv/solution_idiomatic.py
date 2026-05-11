def laenge(liste: list) -> int:
    if not liste:
        return 0
    return 1 + laenge(liste[1:])
