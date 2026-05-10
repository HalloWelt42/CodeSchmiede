"""
Naive Lösung: für jedes Element prüfen, ob es schon in der
Ergebnisliste ist, sonst anhängen.
"""


def ohne_duplikate(zahlen: list) -> list:
    ergebnis = []
    for z in zahlen:
        if z not in ergebnis:
            ergebnis.append(z)
    return ergebnis
