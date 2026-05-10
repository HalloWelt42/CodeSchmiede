"""
List-Comprehension -- der gleiche Algorithmus in einer Zeile.
"""


def chunks(liste: list, n: int) -> list[list]:
    return [liste[i:i + n] for i in range(0, len(liste), n)]
