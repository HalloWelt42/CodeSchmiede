import re


def passwort_ok(p: str) -> bool:
    return bool(re.fullmatch(r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}", p))
