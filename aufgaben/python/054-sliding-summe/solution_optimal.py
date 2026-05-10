"""
Optimal: rollende Summe. O(n).
"""


def max_fenster_summe(zahlen: list[int], k: int) -> int:
    n = len(zahlen)
    if n == 0 or k > n or k <= 0:
        return 0
    aktuell = sum(zahlen[:k])
    bestes = aktuell
    for i in range(k, n):
        aktuell += zahlen[i] - zahlen[i - k]
        if aktuell > bestes:
            bestes = aktuell
    return bestes
