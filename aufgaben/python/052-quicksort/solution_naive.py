"""
Klassisch mit drei expliziten Listen.
"""


def quicksort(liste: list[int]) -> list[int]:
    if len(liste) <= 1:
        return list(liste)
    pivot = liste[0]
    kleiner: list[int] = []
    gleich: list[int] = []
    größer: list[int] = []
    for x in liste:
        if x < pivot:
            kleiner.append(x)
        elif x > pivot:
            größer.append(x)
        else:
            gleich.append(x)
    return quicksort(kleiner) + gleich + quicksort(größer)
