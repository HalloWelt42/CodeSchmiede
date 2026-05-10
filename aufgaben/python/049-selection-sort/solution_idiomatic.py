"""
Idiomatisch mit min() + index() -- nutzt die Standardbibliothek.
"""


def selection_sort(liste: list[int]) -> list[int]:
    a = list(liste)
    for i in range(len(a)):
        min_idx = i + a[i:].index(min(a[i:]))
        a[i], a[min_idx] = a[min_idx], a[i]
    return a
