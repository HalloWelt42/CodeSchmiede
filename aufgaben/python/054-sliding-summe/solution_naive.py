"""
Naive Loesung: jedes Fenster komplett neu summieren. O(n*k).
"""


def max_fenster_summe(zahlen: list[int], k: int) -> int:
    n = len(zahlen)
    if n == 0 or k > n or k <= 0:
        return 0
    bestes = sum(zahlen[:k])
    for i in range(1, n - k + 1):
        s = sum(zahlen[i:i + k])
        if s > bestes:
            bestes = s
    return bestes
