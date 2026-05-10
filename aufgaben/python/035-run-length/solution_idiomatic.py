"""
Mit itertools.groupby -- kompakt und ausdrucksstark.
"""

from itertools import groupby


def rle(text: str) -> str:
    teile: list[str] = []
    for zeichen, gruppe in groupby(text):
        anzahl = sum(1 for _ in gruppe)
        teile.append(zeichen if anzahl == 1 else f"{zeichen}{anzahl}")
    return "".join(teile)
