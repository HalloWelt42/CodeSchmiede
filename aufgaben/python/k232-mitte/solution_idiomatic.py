def binaer(liste, ziel):
    links, rechts = 0, len(liste) - 1
    schritte = 0
    while links <= rechts:
        schritte += 1
        mitte = (links + rechts) // 2
        if liste[mitte] == ziel:
            return mitte, schritte
        if liste[mitte] < ziel:
            links = mitte + 1
        else:
            rechts = mitte - 1
    return -1, schritte


print(binaer([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 23))
