def min_max_index(liste: list) -> list[int]:
    if not liste:
        return [-1, -1]
    return [liste.index(min(liste)), liste.index(max(liste))]
