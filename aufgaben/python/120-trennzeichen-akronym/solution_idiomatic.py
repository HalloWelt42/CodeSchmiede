import re


def akronym_plus(text: str) -> str:
    # camelCase aufsplitten: vor Großbuchstaben einen Trenner einfügen
    mit_trenner = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", text)
    teile = re.split(r"[\s_\-,]+", mit_trenner)
    return "".join(t[0].upper() for t in teile if t)
