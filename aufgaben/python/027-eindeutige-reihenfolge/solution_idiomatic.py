"""
Eine Zeile -- nutzt aus, dass dict seit Python 3.7 die Insertion-Order
garantiert.
"""


def eindeutige(a: list) -> list:
    return list(dict.fromkeys(a))
