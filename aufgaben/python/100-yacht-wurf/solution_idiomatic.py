from collections import Counter


_ZAHLEN = {"ones": 1, "twos": 2, "threes": 3, "fours": 4, "fives": 5, "sixes": 6}


def yacht_punkte(wurf: list[int], kategorie: str) -> int:
    z = Counter(wurf)
    if kategorie in _ZAHLEN:
        wert = _ZAHLEN[kategorie]
        return z.get(wert, 0) * wert
    if kategorie == "full_house":
        werte = sorted(z.values())
        if werte == [2, 3]:
            return sum(wurf)
        return 0
    if kategorie == "four_of_a_kind":
        for wert, anz in z.items():
            if anz >= 4:
                return 4 * wert
        return 0
    if kategorie == "little_straight":
        return 30 if set(wurf) == {1, 2, 3, 4, 5} else 0
    if kategorie == "big_straight":
        return 30 if set(wurf) == {2, 3, 4, 5, 6} else 0
    if kategorie == "choice":
        return sum(wurf)
    if kategorie == "yacht":
        return 50 if len(z) == 1 else 0
    return 0
