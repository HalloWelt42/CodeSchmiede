"""
Eine-Zeilen-Loesung mit Dict-Comprehension.
"""


def invertiere(d: dict) -> dict:
    return {str(v): k for k, v in d.items()}
