"""
Klassische Schleife mit Slicing.
"""


def zaehle_vorkommen(text: str, sub: str) -> int:
    if not sub:
        return 0
    n, m = len(text), len(sub)
    anzahl = 0
    for i in range(n - m + 1):
        if text[i:i + m] == sub:
            anzahl += 1
    return anzahl
