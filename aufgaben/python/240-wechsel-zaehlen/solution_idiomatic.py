def wechsel(liste: list) -> int:
    return sum(1 for a, b in zip(liste, liste[1:]) if a != b)
