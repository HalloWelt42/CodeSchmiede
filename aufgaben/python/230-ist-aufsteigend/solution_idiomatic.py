def ist_aufsteigend(liste: list) -> bool:
    return all(a <= b for a, b in zip(liste, liste[1:]))
