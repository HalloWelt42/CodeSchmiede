"""
Idiomatische Lösung: split() ohne Argument splittet an beliebigem
Whitespace und entfernt führende/abschließende Leerzeichen automatisch.
"""


def erstes_wort(text: str) -> str:
    teile = text.split()
    return teile[0] if teile else ""
