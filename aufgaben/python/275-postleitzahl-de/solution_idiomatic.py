import re


def ist_plz(s: str) -> bool:
    return bool(re.fullmatch(r"\d{5}", s))
