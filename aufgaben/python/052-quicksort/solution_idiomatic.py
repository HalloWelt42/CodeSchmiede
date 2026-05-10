"""
Pythonic mit Comprehensions in einer kompakten Funktion.
"""


def quicksort(liste: list[int]) -> list[int]:
    if len(liste) <= 1:
        return list(liste)
    pivot = liste[len(liste) // 2]
    kleiner = [x for x in liste if x < pivot]
    gleich = [x for x in liste if x == pivot]
    größer = [x for x in liste if x > pivot]
    return quicksort(kleiner) + gleich + quicksort(größer)
