import re


def datum_parse(s: str) -> list[int]:
    m = re.fullmatch(r"(\d{1,2})\.(\d{1,2})\.(\d{4})", s)
    if not m:
        return []
    return [int(x) for x in m.groups()]
