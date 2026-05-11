def max_tiefe(text: str) -> int:
    tiefe = bestes = 0
    for c in text:
        if c == "(":
            tiefe += 1
            if tiefe > bestes:
                bestes = tiefe
        elif c == ")":
            tiefe -= 1
    return bestes
