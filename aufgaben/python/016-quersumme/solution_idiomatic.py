"""
Idiomatische Loesung: rein numerisch mit Modulo und ganzzahliger
Division. Vermeidet die Konvertierung nach String und ist daher
unabhaengig von der Stringdarstellung.
"""


def quersumme(n: int) -> int:
    summe = 0
    while n > 0:
        summe += n % 10
        n //= 10
    return summe
