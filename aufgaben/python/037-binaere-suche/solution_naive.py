"""
Klassisch iterativ.
"""


def binaere_suche(liste: list[int], ziel: int) -> int:
    links, rechts = 0, len(liste) - 1
    while links <= rechts:
        mitte = (links + rechts) // 2
        if liste[mitte] == ziel:
            return mitte
        if liste[mitte] < ziel:
            links = mitte + 1
        else:
            rechts = mitte - 1
    return -1
