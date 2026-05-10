"""
Naive Lösung: Wandle die Zahl in einen String und summiere die
einzelnen Ziffern.
"""


def quersumme(n: int) -> int:
    summe = 0
    for ziffer in str(n):
        summe += int(ziffer)
    return summe
