"""
Klassisches Sieb des Eratosthenes -- O(n log log n).
"""


def primzahlen_bis(n: int) -> list[int]:
    if n < 2:
        return []
    ist_prim = [True] * (n + 1)
    ist_prim[0] = ist_prim[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if ist_prim[i]:
            for k in range(i * i, n + 1, i):
                ist_prim[k] = False
    return [i for i in range(n + 1) if ist_prim[i]]
