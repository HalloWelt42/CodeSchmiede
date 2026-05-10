"""
Kompakter mit max() ueber laufenden Werten.
"""


def laengste_aufsteigend(liste: list[int]) -> int:
    if not liste:
        return 0
    bestes = aktuell = 1
    for vorher, jetzt in zip(liste, liste[1:]):
        aktuell = aktuell + 1 if jetzt > vorher else 1
        bestes = max(bestes, aktuell)
    return bestes
