import re


def zahlen_extrahieren(text: str) -> list[int]:
    return [int(s) for s in re.findall(r"-?\d+", text)]
