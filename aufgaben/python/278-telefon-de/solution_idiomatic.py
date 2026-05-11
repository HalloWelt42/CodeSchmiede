import re


def ist_telefon_de(s: str) -> bool:
    return bool(re.fullmatch(r"(?:\+49 |0)\d{2,5}[ /]\d{4,}", s))
