"""
Trick: Ersetze die Subtraktions-Paare und summiere dann.
Spart die Vergleichsschleife.
"""


def roemisch_zu_int(s: str) -> int:
    paare = [("CM", 900), ("CD", 400), ("XC", 90), ("XL", 40), ("IX", 9), ("IV", 4)]
    werte = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    summe = 0
    for paar, wert in paare:
        anzahl = s.count(paar)
        summe += anzahl * wert
        s = s.replace(paar, "")
    for c in s:
        summe += werte[c]
    return summe
