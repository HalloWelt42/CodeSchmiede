"""
Klassische Schleife mit zwei Zaehlern.
"""


def laengste_aufsteigend(liste: list[int]) -> int:
    if not liste:
        return 0
    aktuell = 1
    bestes = 1
    for i in range(1, len(liste)):
        if liste[i] > liste[i - 1]:
            aktuell += 1
            if aktuell > bestes:
                bestes = aktuell
        else:
            aktuell = 1
    return bestes
