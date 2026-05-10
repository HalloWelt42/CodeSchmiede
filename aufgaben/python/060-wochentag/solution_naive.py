"""
Direkte Umsetzung der Zeller-Formel.
"""


def wochentag(jahr: int, monat: int, tag: int) -> int:
    if monat < 3:
        monat += 12
        jahr -= 1
    k = jahr % 100
    j = jahr // 100
    h = (tag + (13 * (monat + 1)) // 5 + k + k // 4 + j // 4 + 5 * j) % 7
    # Zeller: 0 = Samstag. Wir wollen 0 = Sonntag.
    return (h + 6) % 7
