def ip_zusammen(zahlen: list[int]) -> str:
    if len(zahlen) != 4:
        return ""
    if not all(0 <= x <= 255 for x in zahlen):
        return ""
    return ".".join(str(x) for x in zahlen)
