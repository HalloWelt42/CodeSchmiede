"""
Klassische Implementierung mit Hilfsfunktion merge.
"""


def _merge(a: list[int], b: list[int]) -> list[int]:
    ergebnis: list[int] = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            ergebnis.append(a[i])
            i += 1
        else:
            ergebnis.append(b[j])
            j += 1
    ergebnis.extend(a[i:])
    ergebnis.extend(b[j:])
    return ergebnis


def merge_sort(liste: list[int]) -> list[int]:
    if len(liste) <= 1:
        return list(liste)
    mitte = len(liste) // 2
    links = merge_sort(liste[:mitte])
    rechts = merge_sort(liste[mitte:])
    return _merge(links, rechts)
