"""
Lehrbuch-Variante mit innerem Index-Such-Loop.
"""


def selection_sort(liste: list[int]) -> list[int]:
    a = list(liste)
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a
