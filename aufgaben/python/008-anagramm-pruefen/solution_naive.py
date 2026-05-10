"""
Naive Lösung: für jedes Zeichen in `a` das Vorkommen in `b` prüfen
und entfernen. Wenn `b` leer endet und gleiche Länge -- Anagramm.
"""


def ist_anagramm(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False
    rest = list(b)
    for c in a:
        if c not in rest:
            return False
        rest.remove(c)
    return len(rest) == 0
