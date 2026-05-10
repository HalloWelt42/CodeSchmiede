"""
Lehrbuch-Variante. Immer alle n*n Vergleiche.
"""


def bubble_sort(liste: list[int]) -> list[int]:
    a = list(liste)
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
