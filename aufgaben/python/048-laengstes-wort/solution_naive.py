"""
Klassische Schleife mit Maximum-Tracking.
"""


def laengstes_wort(text: str) -> str:
    bestes = ""
    for wort in text.split():
        if len(wort) > len(bestes):
            bestes = wort
    return bestes
