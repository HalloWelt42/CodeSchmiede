def verbinden(strings: list[str], trenner: str) -> str:
    if not strings:
        return ""
    out = strings[0]
    for s in strings[1:]:
        out += trenner + s
    return out
