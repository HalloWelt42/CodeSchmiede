"""
sum() ueber Generator -- Pythonic.
"""


def zaehle_gross(text: str) -> int:
    return sum(1 for c in text if c.isupper())
