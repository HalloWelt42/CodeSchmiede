def query_parse(s: str) -> dict:
    if not s:
        return {}
    s = s.lstrip("?")
    if not s:
        return {}
    out: dict = {}
    for paar in s.split("&"):
        if "=" in paar:
            k, v = paar.split("=", 1)
            out[k] = v
        else:
            out[paar] = ""
    return out
