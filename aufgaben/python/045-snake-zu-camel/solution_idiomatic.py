"""
Pythonic mit join + Generator.
"""


def snake_zu_camel(text: str) -> str:
    teile = text.split("_")
    return teile[0] + "".join(t.capitalize() for t in teile[1:])
