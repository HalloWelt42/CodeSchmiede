"""
Mit Early-Exit: ist nichts mehr zu tauschen, ist die Liste sortiert.
Bricht im Best-Case (bereits sortiert) nach einem Durchlauf ab.
"""


def bubble_sort(liste: list[int]) -> list[int]:
    a = list(liste)
    n = len(a)
    for i in range(n):
        getauscht = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                getauscht = True
        if not getauscht:
            break
    return a
