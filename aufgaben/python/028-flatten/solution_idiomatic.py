"""
List-Comprehension -- die Pythonic-Version.
"""


def flatten(liste: list[list]) -> list:
    return [x for innen in liste for x in innen]
