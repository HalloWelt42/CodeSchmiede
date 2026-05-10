"""
Korrekte Variante mit voller Range. Alternativ einfach sum(zahlen).
"""


def summe(zahlen):
    ergebnis = 0
    for i in range(len(zahlen)):
        ergebnis += zahlen[i]
    return ergebnis
