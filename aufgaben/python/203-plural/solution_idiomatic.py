def plural(n: int, singular: str, plural: str) -> str:
    wort = singular if abs(n) == 1 else plural
    return f"{n} {wort}"
