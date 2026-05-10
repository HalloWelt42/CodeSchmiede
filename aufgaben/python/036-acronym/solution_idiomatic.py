"""
Generator + join -- Pythonic.
"""


def akronym(text: str) -> str:
    return "".join(w[0].upper() for w in text.split())
