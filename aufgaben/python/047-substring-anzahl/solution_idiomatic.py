"""
Mit str.find() in Schleife: bei jedem Treffer nur eine Position weiter
suchen, statt um die Substring-Laenge zu springen.
"""


def zaehle_vorkommen(text: str, sub: str) -> int:
    if not sub:
        return 0
    anzahl = 0
    pos = 0
    while True:
        pos = text.find(sub, pos)
        if pos == -1:
            break
        anzahl += 1
        pos += 1
    return anzahl
