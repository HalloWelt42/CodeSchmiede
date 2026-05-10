def ist_ipv4(text: str) -> bool:
    teile = text.split(".")
    if len(teile) != 4:
        return False
    for t in teile:
        if not t.isdigit():
            return False
        if len(t) > 1 and t[0] == "0":
            return False
        if not 0 <= int(t) <= 255:
            return False
    return True
