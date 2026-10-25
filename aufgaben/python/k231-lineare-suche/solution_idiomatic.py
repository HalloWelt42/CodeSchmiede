def suche(liste, ziel):
    for i in range(len(liste)):
        if liste[i] == ziel:
            return i
    return -1


print(suche([4, 9, 2, 7], 2))
