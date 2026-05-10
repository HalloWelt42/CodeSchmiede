"""
Mit "Karte herausheben + Loch verschieben" -- spart Tausche und ist
naeher am Lehrbuch-Pseudocode.
"""


def insertion_sort(liste: list[int]) -> list[int]:
    a = list(liste)
    for i in range(1, len(a)):
        karte = a[i]
        j = i - 1
        while j >= 0 and a[j] > karte:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = karte
    return a
