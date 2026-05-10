"""
Naive Lösung: aufsteigend sortieren, dann umkehren. Funktional
korrekt, aber zwei Schritte statt einem.
"""


def sortiere_absteigend(zahlen: list[int]) -> list[int]:
    aufsteigend = sorted(zahlen)
    return aufsteigend[::-1]
