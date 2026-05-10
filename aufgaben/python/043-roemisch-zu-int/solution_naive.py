"""
Klassische Schleife: vergleiche aktuelles Zeichen mit dem naechsten,
ziehe ab oder addiere entsprechend.
"""


WERT = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roemisch_zu_int(s: str) -> int:
    summe = 0
    n = len(s)
    for i in range(n):
        if i + 1 < n and WERT[s[i]] < WERT[s[i + 1]]:
            summe -= WERT[s[i]]
        else:
            summe += WERT[s[i]]
    return summe
