"""
Slicing -- O(n) und liest sich klar.
"""


def rotiere(liste: list, k: int) -> list:
    if not liste:
        return []
    k = k % len(liste)
    return liste[k:] + liste[:k]
