"""
Naive Lösung: Versuchsdivision durch alle Zahlen von 2 bis n-1.
Funktional korrekt, aber für große n langsam (O(n)).
"""


def ist_primzahl(n: int) -> bool:
    if n < 2:
        return False
    for teiler in range(2, n):
        if n % teiler == 0:
            return False
    return True
