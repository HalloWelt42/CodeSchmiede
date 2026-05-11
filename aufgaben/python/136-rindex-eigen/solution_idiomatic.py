def letztes_vorkommen(liste: list, ziel) -> int:
    for i in range(len(liste) - 1, -1, -1):
        if liste[i] == ziel:
            return i
    return -1
