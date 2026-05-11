def inkrement(s: str) -> str:
    try:
        return str(int(s) + 1)
    except ValueError:
        return ""
