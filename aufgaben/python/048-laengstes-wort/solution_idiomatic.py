"""
Mit max + default für den leeren Fall.
"""


def laengstes_wort(text: str) -> str:
    return max(text.split(), key=len, default="")
