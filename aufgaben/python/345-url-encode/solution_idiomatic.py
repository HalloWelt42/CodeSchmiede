_UNRES = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.~")


def url_encode(s: str) -> str:
    out: list[str] = []
    for byte in s.encode("utf-8"):
        c = chr(byte)
        if c in _UNRES:
            out.append(c)
        else:
            out.append(f"%{byte:02X}")
    return "".join(out)
