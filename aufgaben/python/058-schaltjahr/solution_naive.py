"""
Naive Loesung mit verschachteltem if/else.
"""


def ist_schaltjahr(jahr: int) -> bool:
    if jahr % 4 != 0:
        return False
    if jahr % 100 != 0:
        return True
    if jahr % 400 != 0:
        return False
    return True
